import os
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load data
products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
interactions = pd.read_csv(os.path.join(DATA_DIR, "interactions.csv"))

print(f"Loaded {len(products)} products and {len(interactions)} interactions")

# Encode categories
category_encoder = LabelEncoder()
products["category_encoded"] = category_encoder.fit_transform(
    products["category_code"].fillna("unknown")
)

# Build simple embedding model
n_categories = len(category_encoder.classes_)
embedding_dim = 50

category_input = Input(shape=(1,))
category_embedding = Embedding(n_categories, embedding_dim)(category_input)
flat = Flatten()(category_embedding)
output = Dense(embedding_dim, activation="relu")(flat)

model = Model(inputs=category_input, outputs=output)
model.compile(optimizer=Adam(learning_rate=0.001), loss="mse")

print(f"Embedding model created with {embedding_dim} dimensions")

# Generate embeddings for all products
category_codes = products["category_encoded"].values.reshape(-1, 1)
embeddings = model.predict(category_codes, verbose=0)

print(f"Generated embeddings shape: {embeddings.shape}")

# Save embeddings
content_data = {
    "embeddings": embeddings,
    "product_ids": list(products["product_id"]),
}

with open(os.path.join(MODEL_DIR, "product_embeddings.pkl"), "wb") as f:
    pickle.dump(content_data, f)

print("✅ Embeddings saved to product_embeddings.pkl")
print(f"   Stored {len(content_data['product_ids'])} product embeddings")
