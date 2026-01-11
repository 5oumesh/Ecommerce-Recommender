# API Reference

## Core Modules

### 1. Data Loading (`src/data/load_data.py`)

#### Function: `load_data()`
Load all processed data files.

```python
from src.data.load_data import load_data

interactions, products, users = load_data()

# Returns:
# - interactions: DataFrame with columns [user_id, product_id, event_type, timestamp]
# - products: DataFrame with columns [product_id, name, brand, price, category, ...]
# - users: DataFrame with columns [user_id, total_purchases, favorite_category, ...]
```

**Parameters**: None

**Returns**:
- `interactions`: pd.DataFrame - User-product interactions
- `products`: pd.DataFrame - Product metadata
- `users`: pd.DataFrame - User profiles

---

### 2. Recommendation Engine (`src/inference/recommend.py`)

#### Function: `hybrid_recommend()`
Generate personalized recommendations using hybrid model.

```python
from src.inference.recommend import hybrid_recommend

recommendations = hybrid_recommend(
    user_id=123,
    category='appliances.kitchen',
    n_recommendations=10,
    min_rating=3.0
)

# Returns: List of (product_id, score) tuples, ranked by score
```

**Parameters**:
- `user_id` (int): User identifier
- `category` (str): Product category (format: "main.sub")
- `n_recommendations` (int, default=10): Number of recommendations (1-20)
- `min_rating` (float, default=0.0): Minimum product rating filter

**Returns**:
- List of tuples: `[(product_id, score), ...]`
  - `product_id`: String identifier
  - `score`: Recommendation score (0-1)

**Example**:
```python
recs = hybrid_recommend(user_id=123, category='electronics.smartphone', n_recommendations=5)
for prod_id, score in recs:
    print(f"Product {prod_id}: {score:.4f}")
```

---

#### Function: `get_user_embeddings()`
Get user embedding vector.

```python
from src.inference.recommend import get_user_embeddings

embedding = get_user_embeddings(user_id=123)
# Returns: numpy.ndarray of shape (32,) - User embedding vector
```

---

#### Function: `get_product_similarity()`
Calculate similarity between products.

```python
from src.inference.recommend import get_product_similarity

similarity = get_product_similarity(product_id_1='P123', product_id_2='P456')
# Returns: float (0-1) - Similarity score
```

---

### 3. Model Classes (`src/models/`)

#### Class: `NCFModel`
Neural Collaborative Filtering model.

```python
from src.models.ncf_model import NCFModel

model = NCFModel(
    n_users=35516,
    n_products=14011,
    embedding_dim=32,
    hidden_layers=[256, 128, 64]
)

# Train
model.fit(interactions_matrix, epochs=50, batch_size=32)

# Predict
scores = model.predict(user_ids=[1, 2, 3], product_ids=[1, 2, 3])
```

**Parameters**:
- `n_users` (int): Number of unique users
- `n_products` (int): Number of unique products
- `embedding_dim` (int, default=32): Embedding dimension
- `hidden_layers` (list, default=[256, 128, 64]): Dense layer sizes

**Methods**:
- `fit(interactions, epochs, batch_size)` - Train model
- `predict(user_ids, product_ids)` - Get prediction scores
- `save(path)` - Save model to disk
- `load(path)` - Load model from disk

---

#### Class: `ContentModel`
Content-based recommendation model.

```python
from src.models.content_model import ContentModel

model = ContentModel(embedding_dim=300)

# Fit on product features
model.fit(product_features)

# Get similarity
similarity = model.similarity(product_id_1, product_id_2)
```

---

### 4. Data Preprocessing (`src/data/preprocess.py`)

#### Function: `preprocess_interactions()`
Clean and validate interaction data.

```python
from src.data.preprocess import preprocess_interactions

clean_interactions = preprocess_interactions(
    raw_interactions,
    remove_duplicates=True,
    remove_outliers=True
)
```

**Parameters**:
- `raw_interactions` (DataFrame): Raw interaction data
- `remove_duplicates` (bool, default=True): Remove duplicate interactions
- `remove_outliers` (bool, default=True): Remove extreme values

**Returns**: pd.DataFrame - Cleaned interactions

---

### 5. Evaluation Metrics (`src/evaluations/evaluate.py`)

#### Function: `evaluate_model()`
Compute evaluation metrics.

```python
from src.evaluations.evaluate import evaluate_model

metrics = evaluate_model(
    predictions,
    ground_truth,
    metrics=['hit_rate', 'precision', 'recall', 'f1']
)

print(metrics)
# Output: {'hit_rate': 0.098, 'precision': 0.0098, 'recall': 0.098, 'f1': 0.0178}
```

**Parameters**:
- `predictions` (list): Model predictions
- `ground_truth` (list): True labels
- `metrics` (list): Metrics to compute

**Returns**: dict - Metric name → value

---

## User Interface Classes

### EcommerceNavigator (`ecommerce_navigator.py`)

Main interactive navigation system.

```python
from ecommerce_navigator import EcommerceNavigator

navigator = EcommerceNavigator()
navigator.run()
```

**Key Methods**:
- `run()` - Start interactive session
- `display_main_categories()` - Show all main categories
- `get_main_category_selection()` - Get user's main category choice
- `display_subcategories(main_cat)` - Show subcategories for main category
- `get_subcategory_selection()` - Get user's subcategory choice
- `get_recommendation_count()` - Ask for number of recommendations
- `display_recommendations(products)` - Show results in formatted table

---

## Data Structures

### Interaction Format
```python
{
    'user_id': int,
    'product_id': str,
    'event_type': str,  # 'view', 'purchase', 'cart_add'
    'timestamp': datetime,
    'price': float
}
```

### Product Format
```python
{
    'product_id': str,
    'name': str,
    'brand': str,
    'price': float,
    'category': str,  # Format: 'main.subcategory'
    'rating': float,
    'popularity_score': int
}
```

### User Format
```python
{
    'user_id': int,
    'total_interactions': int,
    'total_purchases': int,
    'favorite_category': str,
    'favorite_brand': str,
    'activity_level': str  # 'high', 'medium', 'low'
}
```

### Recommendation Format
```python
[
    (product_id_1, score_1),  # score: 0-1
    (product_id_2, score_2),
    ...
]
```

---

## Configuration

### Global Settings

Create `config.py` in project root:

```python
# Model configuration
MODEL_CONFIG = {
    'embedding_dim': 32,
    'hidden_layers': [256, 128, 64],
    'dropout_rate': 0.3,
    'learning_rate': 0.001
}

# Recommendation configuration
RECOMMENDATION_CONFIG = {
    'ncf_weight': 0.7,
    'content_weight': 0.3,
    'default_n_recommendations': 10,
    'max_recommendations': 20
}

# Data configuration
DATA_CONFIG = {
    'processed_data_path': 'data/processed/',
    'models_path': 'models/',
    'cache_embeddings': True
}
```

---

## Error Handling

### Common Exceptions

```python
from src.inference.recommend import RecommendationError, ModelLoadError

try:
    recommendations = hybrid_recommend(user_id=999, category='invalid')
except RecommendationError as e:
    print(f"Recommendation error: {e}")
except ModelLoadError as e:
    print(f"Model error: {e}")
```

---

## Performance Tips

1. **Batch Processing**: Use batch operations for multiple users
   ```python
   # Slow
   for user_id in user_list:
       recs = hybrid_recommend(user_id)
   
   # Fast
   recs_batch = batch_recommend(user_list, n_recommendations=10)
   ```

2. **Caching**: Pre-load embeddings
   ```python
   from src.inference.recommend import load_embeddings
   load_embeddings()  # Cache to memory
   ```

3. **Category Filtering**: Use specific categories
   ```python
   # More specific = faster
   hybrid_recommend(user_id=123, category='appliances.kitchen')
   ```

---

## Examples

### Example 1: Get Recommendations for User
```python
from src.inference.recommend import hybrid_recommend
from src.data.load_data import load_data

interactions, products, users = load_data()

# Get 5 kitchen appliance recommendations for user 123
recs = hybrid_recommend(
    user_id=123,
    category='appliances.kitchen',
    n_recommendations=5
)

# Display results
for prod_id, score in recs:
    product = products[products['product_id'] == prod_id].iloc[0]
    print(f"{product['name']}: {score:.4f} (Brand: {product['brand']})")
```

### Example 2: Batch Recommendations
```python
from src.inference.recommend import batch_recommend

user_ids = [1, 2, 3, 4, 5]
recommendations = batch_recommend(
    user_ids=user_ids,
    category='electronics.smartphone',
    n_recommendations=10
)

# recommendations: dict of {user_id: [(prod_id, score), ...]}
```

### Example 3: Evaluate Model
```python
from src.evaluations.evaluate import evaluate_model

predictions = [...]  # Model predictions
ground_truth = [...]  # True labels

metrics = evaluate_model(
    predictions,
    ground_truth,
    metrics=['hit_rate', 'precision', 'recall', 'f1', 'ndcg']
)

print(f"Hit Rate: {metrics['hit_rate']:.4f}")
print(f"Precision: {metrics['precision']:.4f}")
print(f"Recall: {metrics['recall']:.4f}")
print(f"F1 Score: {metrics['f1']:.4f}")
```

---

**For more information, see README.md and notebooks/**

