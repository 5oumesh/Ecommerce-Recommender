import os
import pickle
import numpy as np
import pandas as pd

from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# data
products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
interactions = pd.read_csv(os.path.join(DATA_DIR, "interactions.csv"))
interactions = interactions[interactions["event_type"] == "purchase"]

# content embeddings
with open(os.path.join(MODEL_DIR, "product_embeddings.pkl"), "rb") as f:
    content_data = pickle.load(f)

product_ids = content_data["product_ids"]
product_embeddings = np.asarray(content_data["embeddings"])

product_id_to_index = {pid: i for i, pid in enumerate(product_ids)}

# CF model
cf_model = load_model(os.path.join(MODEL_DIR, "ncf_model.h5"), compile=False)

# encoders
with open(os.path.join(MODEL_DIR, "user_encoder.pkl"), "rb") as f:
    user_encoder = pickle.load(f)

with open(os.path.join(MODEL_DIR, "product_encoder.pkl"), "rb") as f:
    product_encoder = pickle.load(f)

def content_recommend(seed_product_id, top_n=20):
    if seed_product_id not in product_id_to_index:
        return []

    idx = product_id_to_index[seed_product_id]
    sim = cosine_similarity(
        product_embeddings[idx].reshape(1, -1),
        product_embeddings
    )[0]

    top_idx = sim.argsort()[-top_n-1:][::-1][1:]
    return [product_ids[i] for i in top_idx]


def cf_recommend(user_id, top_n=20):
    if user_id not in user_encoder.classes_:
        return []

    u = user_encoder.transform([user_id])[0]
    p_enc = np.arange(len(product_encoder.classes_))
    u_arr = np.full(len(p_enc), u)

    scores = cf_model.predict([u_arr, p_enc], verbose=0).flatten()
    top_idx = scores.argsort()[-top_n:][::-1]
    return [product_encoder.inverse_transform(top_idx)[i] for i in range(len(top_idx))]


def hybrid_recommend(user_id, seed_product_id, top_n=10):
    content = set(content_recommend(seed_product_id, 100))
    cf = set(cf_recommend(user_id, 100))

    scored = []
    for pid in content | cf:
        score = (0.3 if pid in content else 0) + (0.7 if pid in cf else 0)
        scored.append((pid, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return [pid for pid, _ in scored[:top_n]]

# group interactions by user
user_groups = interactions.groupby("user_id")

K = 10
hits = 0
total = 0
relevant_items_per_user = 0

print("\n🔄 Evaluating recommendations...")
print("=" * 60)

for user_id, group in user_groups:
    if len(group) < 2:
        continue

    # last interaction = ground truth
    test_item = group.iloc[-1]["product_id"]
    seed_item = group.iloc[0]["product_id"]

    recs = hybrid_recommend(user_id, seed_item, top_n=K)

    if test_item in recs:
        hits += 1

    relevant_items_per_user += 1
    total += 1

    if total >= 500:   # limit for speed
        break

# Calculate comprehensive metrics
hit_rate = hits / total if total > 0 else 0
precision_at_k = hits / (total * K) if total > 0 else 0
recall_at_k = hits / relevant_items_per_user if relevant_items_per_user > 0 else 0

# F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
if precision_at_k + recall_at_k > 0:
    f1_score = 2 * (precision_at_k * recall_at_k) / (precision_at_k + recall_at_k)
else:
    f1_score = 0

# Calculate Hit Rate as percentage
hit_rate_percent = hit_rate * 100

print(f"\n📊 EVALUATION METRICS (K={K})")
print("=" * 60)
print(f"Users evaluated:        {total}")
print(f"Recommendations made:   {total * K}")
print(f"Relevant hits:          {hits}")
print("=" * 60)
print(f"\n✅ Performance Metrics:")
print(f"   Hit Rate@{K}:         {hit_rate:.4f} ({hit_rate_percent:.2f}%)")
print(f"   Precision@{K}:        {precision_at_k:.4f} ({precision_at_k*100:.2f}%)")
print(f"   Recall@{K}:           {recall_at_k:.4f} ({recall_at_k*100:.2f}%)")
print(f"   F1 Score:             {f1_score:.4f}")
print("=" * 60)

# Interpretation
print(f"\n💡 Interpretation:")
print(f"   • Hit Rate: {hit_rate_percent:.1f}% of users got at least 1 relevant item")
print(f"   • Precision: {precision_at_k*100:.2f}% of recommendations are relevant")
print(f"   • Recall: {recall_at_k*100:.2f}% of relevant items were recommended")
print(f"   • F1 Score: Balanced performance metric ({f1_score:.4f})")
print("=" * 60)
