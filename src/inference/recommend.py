import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import numpy as np
import pandas as pd
import pickle

from tensorflow.keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
interactions = pd.read_csv(os.path.join(DATA_DIR, "interactions.csv"))

with open(os.path.join(MODEL_DIR, "product_embeddings.pkl"), "rb") as f:
    content_data = pickle.load(f)

product_embeddings = content_data['embeddings']
product_ids = list(content_data['product_ids'])


cf_model = load_model(
    os.path.join(MODEL_DIR, "ncf_model.h5"),
    compile=False
)


with open(os.path.join(MODEL_DIR, "user_encoder.pkl"), "rb") as f:
    user_encoder = pickle.load(f)

with open(os.path.join(MODEL_DIR, "product_encoder.pkl"), "rb") as f:
    product_encoder = pickle.load(f)


print("Models and data loaded")

product_id_to_index = {
    pid: idx for idx, pid in enumerate(products["product_id"])
}


def content_recommend(seed_product_id, top_n=20):
    if seed_product_id not in product_ids:
        return []

    idx = product_ids.index(seed_product_id)

    sim_scores = cosine_similarity(
        product_embeddings[idx].reshape(1, -1),
        product_embeddings
    )[0]

    top_indices = sim_scores.argsort()[-top_n-1:][::-1][1:]
    return [product_ids[i] for i in top_indices]


def cf_recommend(user_id, top_n=20):
    if user_id not in user_encoder.classes_:
        return []

    user_enc = user_encoder.transform([user_id])[0]

    product_encs = np.arange(len(product_encoder.classes_))
    user_array = np.full(len(product_encs), user_enc)

    scores = cf_model.predict(
        [user_array, product_encs],
        verbose=0
    ).flatten()

    top_idx = scores.argsort()[-top_n:][::-1]
    return product_encoder.inverse_transform(top_idx)

def hybrid_recommend(user_id, seed_product_id, top_n=10):
    content_recs = set()
    if seed_product_id in product_id_to_index:
        content_recs = set(content_recommend(seed_product_id, top_n=30))

        cf_recs = set(cf_recommend(user_id, top_n=30))

        combined = list(content_recs | cf_recs)

        scores = []

        for pid in combined:
            score = 0

            if pid in content_recs:
                score += 0.4
            if pid in cf_recs:
                score += 0.6

            scores.append((pid, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        final_products = [pid for pid, _ in scores[:top_n]]

        return products[
            products["product_id"].isin(final_products)
        ]

# Pick a sample user and product from interactions
sample_user = interactions["user_id"].iloc[0]
sample_product = interactions["product_id"].iloc[0]

print("User:", sample_user)
print("Seed Product:", sample_product)

recommendations = hybrid_recommend(
    user_id=sample_user,
    seed_product_id=sample_product,
    top_n=5
)

print("\nRecommended Products:")
print(recommendations)

print("Embeddings type:", type(product_embeddings))
print("Embeddings shape:", product_embeddings.shape)

recommendations.to_csv(
    os.path.join(BASE_DIR, "outputs", "recommendations.csv"),
    index=False
)
print("Recommendations saved to outputs/recommendations.csv")

