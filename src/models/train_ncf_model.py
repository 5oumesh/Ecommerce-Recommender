import os
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Input, Embedding, Flatten, Concatenate, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load data
interactions = pd.read_csv(os.path.join(DATA_DIR, "interactions.csv"))

print(f"Loaded {len(interactions)} interactions")

# Use only purchase interactions for stronger signal
interactions = interactions[interactions["event_type"] == "purchase"]
print(f"Using {len(interactions)} purchase interactions")

# Encode users and products
user_encoder = LabelEncoder()
product_encoder = LabelEncoder()

interactions["user_encoded"] = user_encoder.fit_transform(interactions["user_id"])
interactions["product_encoded"] = product_encoder.fit_transform(interactions["product_id"])

n_users = len(user_encoder.classes_)
n_products = len(product_encoder.classes_)
embedding_dim = 50

print(f"Users: {n_users}, Products: {n_products}, Embedding dim: {embedding_dim}")

# Build Neural Collaborative Filtering model
user_input = Input(shape=(1,))
product_input = Input(shape=(1,))

user_embedding = Embedding(n_users, embedding_dim)(user_input)
product_embedding = Embedding(n_products, embedding_dim)(product_input)

user_flat = Flatten()(user_embedding)
product_flat = Flatten()(product_embedding)

concat = Concatenate()([user_flat, product_flat])
dense1 = Dense(128, activation="relu")(concat)
dense2 = Dense(64, activation="relu")(dense1)
dense3 = Dense(32, activation="relu")(dense2)
output = Dense(1, activation="sigmoid")(dense3)

model = Model(inputs=[user_input, product_input], outputs=output)
model.compile(optimizer=Adam(learning_rate=0.001), loss="binary_crossentropy", metrics=["accuracy"])

print("NCF model built and compiled")

# Prepare training data
X_user = interactions["user_encoded"].values
X_product = interactions["product_encoded"].values
y = np.ones(len(interactions))  # All are positive interactions (purchases)

# Train model
early_stop = EarlyStopping(monitor="loss", patience=2, restore_best_weights=True)

history = model.fit(
    [X_user, X_product],
    y,
    epochs=10,
    batch_size=256,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

print("✅ NCF model trained")

# Save model
model.save(os.path.join(MODEL_DIR, "ncf_model.h5"))
print("   Saved to ncf_model.h5")

# Save encoders
with open(os.path.join(MODEL_DIR, "user_encoder.pkl"), "wb") as f:
    pickle.dump(user_encoder, f)
with open(os.path.join(MODEL_DIR, "product_encoder.pkl"), "wb") as f:
    pickle.dump(product_encoder, f)

print("   Saved encoders")
