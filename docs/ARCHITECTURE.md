# Architecture & Design

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│             E-COMMERCE RECOMMENDATION SYSTEM                │
└─────────────────────────────────────────────────────────────┘

  ┌─ Presentation Layer ────────────────────────────────────┐
  │ ┌──────────────────────────────────────────────────────┐│
  │ │  launcher.py          ecommerce_navigator.py          ││
  │ │  DEMO_NAVIGATOR.py    QUICK_REFERENCE.py             ││
  │ └──────────────────────────────────────────────────────┘│
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─ Business Logic Layer ──────────────────────────────────┐
  │ ┌──────────────────────────────────────────────────────┐│
  │ │  src/inference/recommend.py                          ││
  │ │  • hybrid_recommend()                                ││
  │ │  • batch_recommend()                                 ││
  │ │  • Combines NCF (70%) + Content (30%)                ││
  │ └──────────────────────────────────────────────────────┘│
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─ Model Layer ───────────────────────────────────────────┐
  │ ┌──────────────────────────────────────────────────────┐│
  │ │ NCF Model              Content Model                  ││
  │ │ • Embeddings (32D)     • Embeddings (300D)            ││
  │ │ • Dense layers         • Cosine similarity            ││
  │ │ • Trained on 179K      • Pre-trained on features      ││
  │ └──────────────────────────────────────────────────────┘│
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─ Data Layer ────────────────────────────────────────────┐
  │ ┌──────────────────────────────────────────────────────┐│
  │ │  src/data/load_data.py                               ││
  │ │  src/data/preprocess.py                              ││
  │ │  • Load interactions.csv                             ││
  │ │  • Load products.csv                                 ││
  │ │  • Load users.csv                                    ││
  │ └──────────────────────────────────────────────────────┘│
  └─────────────────────────────────────────────────────────┘
                            ↓
  ┌─ Storage Layer ─────────────────────────────────────────┐
  │ ┌──────────────────────────────────────────────────────┐│
  │ │  data/processed/ (CSV files)                         ││
  │ │  models/ (Model + embeddings)                        ││
  │ └──────────────────────────────────────────────────────┘│
  └─────────────────────────────────────────────────────────┘
```

---

## Component Details

### 1. Presentation Layer

#### `launcher.py`
- **Purpose**: Menu-driven entry point
- **Features**: 
  - 5-option menu system
  - User-friendly prompts
  - Subprocess management
- **Flow**: Menu → Option selection → Delegate to appropriate module

#### `ecommerce_navigator.py`
- **Purpose**: Main interactive navigation system
- **Features**:
  - 3-level hierarchical browsing
  - Category hierarchy parsing
  - Recommendation display
- **Flow**: 
  1. Load data & build hierarchy
  2. Show main categories
  3. Get user selection
  4. Show subcategories
  5. Get user selection
  6. Generate recommendations
  7. Display results
  8. Ask for next action (another/back/quit)

#### `DEMO_NAVIGATOR.py` & `QUICK_REFERENCE.py`
- **Purpose**: Educational/reference materials
- **Features**: Visual examples, quick guides

---

### 2. Business Logic Layer

#### `src/inference/recommend.py`

**Main Function: `hybrid_recommend()`**

```python
def hybrid_recommend(user_id, category, n_recommendations=10):
    # Step 1: Load models and data
    ncf_model = load_ncf_model()
    product_embeddings = load_embeddings()
    category_products = filter_by_category(category)
    
    # Step 2: Get user history
    user_history = get_user_purchase_history(user_id)
    
    # Step 3: NCF Scoring
    ncf_scores = ncf_model.predict(
        user_id=user_id,
        product_ids=category_products
    )
    
    # Step 4: Content-Based Scoring
    content_scores = calculate_content_similarity(
        user_history_products=user_history,
        candidate_products=category_products
    )
    
    # Step 5: Hybrid Combination
    hybrid_scores = (0.7 * ncf_scores) + (0.3 * content_scores)
    
    # Step 6: Rank and Return Top-N
    ranked_products = sorted(hybrid_scores.items(), 
                            key=lambda x: x[1], 
                            reverse=True)
    
    return ranked_products[:n_recommendations]
```

**Scoring Formula**:
```
Hybrid_Score = (0.7 × NCF_Score) + (0.3 × Content_Score)

Where:
- NCF_Score: Neural Collaborative Filtering prediction (0-1)
  └─ Learns from similar users' purchases
  
- Content_Score: Content-based similarity (0-1)
  └─ Similarity of product features to user's history
```

---

### 3. Model Layer

#### Neural Collaborative Filtering (NCF)

**Architecture**:
```
User Input (ID)
    ↓
Embedding Layer (32 dims)
    ↓
Dropout (0.3)
    ↓              
Concatenate ──→ Dense(256) → ReLU → Dropout(0.3)
    ↑                          ↓
Dropout (0.3)         Dense(128) → ReLU → Dropout(0.3)
    ↑                          ↓
Product Input (ID)    Dense(64) → ReLU
Embedding Layer (32 dims)
    ↓              
Dropout (0.3)
    ↓
                            ↓
                    Output (1 node) 
                    Sigmoid → [0, 1]
```

**Training Details**:
- **Loss Function**: Binary Crossentropy
- **Optimizer**: Adam (lr=0.001)
- **Batch Size**: 32
- **Epochs**: 50
- **Validation Split**: 0.2

**Training Process**:
1. Create user-product interaction matrix (35.5K × 14K sparse matrix)
2. Split into train (80%) and test (20%)
3. Train NCF on train set
4. Evaluate on test set
5. Save best model

#### Content-Based Model

**Features Used**:
- Brand (1-hot encoded)
- Price (normalized)
- Category (hierarchical)
- View count
- Purchase count
- Popularity score

**Similarity Calculation**:
```python
similarity = cosine_similarity(
    user_history_embedding,  # 300D vector
    candidate_embedding       # 300D vector
)
```

**Embedding Generation**:
- Use pre-trained word embeddings for categorical features
- Normalize numerical features
- Concatenate all features → 300D vector
- Apply PCA if needed for dimensionality reduction

---

### 4. Data Layer

#### Data Loading Flow

```
Raw CSV Files
    ↓
Load with Pandas
    ↓
Validate Schema
    ↓
Check for Missing Values
    ↓
Merge Tables (interactions + products)
    ↓
Cache in Memory
    ↓
Ready for Processing
```

#### Data Preprocessing

```
Raw Interactions (42.4M rows)
    ↓
Sample (1M rows per chunk)
    ↓
Remove Duplicates
    ↓
Remove Outliers
    ↓
Enrich Features
    ↓
Clean Interactions (179.5K)
    ↓
Extract User & Product Features
    ↓
Create Category Hierarchy
```

---

## Data Flow

### Recommendation Request Flow

```
User Input (user_id, category, n_recs)
    ↓
Load NCF Model (from disk/cache)
    ↓
Load Product Embeddings (from disk/cache)
    ↓
Filter Products by Category
    ↓
Generate NCF Scores
    ↓
Generate Content Scores
    ↓
Combine (Hybrid Scoring)
    ↓
Sort & Rank
    ↓
Return Top-N
    ↓
Display to User
```

### Training Flow

```
Raw Data (42.4M rows)
    ↓
Data Cleaning
    ↓
Feature Engineering (49.6s)
    ↓
Split Train/Test (80/20)
    ↓
Train NCF Model
    ↓
Train Content Model
    ↓
Evaluate Metrics
    ↓
Save Models
    ↓
Ready for Inference
```

---

## Caching Strategy

### Memory Caching

```python
# Models cached on first load
_ncf_model = None
_embeddings = None

def load_ncf_model():
    global _ncf_model
    if _ncf_model is None:
        _ncf_model = load_from_disk('models/ncf_model.h5')
    return _ncf_model

def load_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = load_from_disk('models/product_embeddings.pkl')
    return _embeddings
```

**Benefits**:
- First recommendation: ~1-2 seconds (load time)
- Subsequent: <4ms (cache lookup)

### Category Cache

```python
# Category hierarchy cached on startup
_category_hierarchy = None

def build_category_hierarchy():
    global _category_hierarchy
    if _category_hierarchy is None:
        _category_hierarchy = parse_categories_from_data()
    return _category_hierarchy
```

---

## Error Handling

### Exception Hierarchy

```python
class RecommendationError(Exception):
    """Base exception for recommendation errors"""
    pass

class ModelLoadError(RecommendationError):
    """Model loading failed"""
    pass

class DataError(RecommendationError):
    """Data loading/processing error"""
    pass

class CategoryError(RecommendationError):
    """Invalid category specified"""
    pass

class UserError(RecommendationError):
    """User not found or invalid"""
    pass
```

### Error Handling Flow

```python
try:
    recommendations = hybrid_recommend(user_id, category)
except ModelLoadError:
    # Handle model loading failure
    # Return fallback recommendations
except DataError:
    # Handle data loading failure
    # Log error and notify user
except CategoryError:
    # Handle invalid category
    # Show valid categories
except UserError:
    # Handle user not found
    # Use content-based fallback
except Exception as e:
    # Unexpected error
    # Log and return empty result
```

---

## Performance Optimization

### 1. Vectorized Operations

```python
# Slow (row iteration)
for idx, row in df.iterrows():
    process(row)

# Fast (vectorized)
result = df.apply(vectorized_function, axis=1)
```

### 2. Chunked Processing

```python
chunk_size = 1_000_000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    process_chunk(chunk)
```

**Result**: 84% speedup (300s → 49.6s)

### 3. Embedding Caching

Pre-compute and cache 300D product embeddings to avoid recalculation.

### 4. Model Quantization

Option to quantize NCF model for faster inference on edge devices.

---

## Scalability Considerations

### Current Scale
- Users: 35K
- Products: 14K
- Interactions: 179K
- Latency: <4ms per recommendation

### Scaling to 1M+ Users

```
1. Distributed NCF Training
   └─ Use Horovod or Ray for distributed training
   
2. Embedding Server
   └─ Separate service for embedding lookups
   └─ Use Redis for fast in-memory caching
   
3. Batch Processing
   └─ Generate recommendations in batches
   └─ Use message queues (Kafka/RabbitMQ)
   
4. Model Serving
   └─ Use TensorFlow Serving
   └─ Deploy with Kubernetes
```

---

## Deployment Architecture

### Development
```
Single Machine
├─ Jupyter Notebooks (training)
├─ Python scripts (testing)
└─ Local data files
```

### Production
```
Microservices
├─ API Service (FastAPI/Flask)
│  └─ Health checks, logging, monitoring
├─ Recommendation Service
│  └─ Model inference, caching
├─ Data Service
│  └─ Data loading, validation
└─ Cache Layer (Redis)
   └─ Embeddings, model weights

Load Balancer → Multiple Service Replicas → Database
```

---

## Testing Strategy

### Unit Tests
```python
def test_hybrid_recommend():
    recs = hybrid_recommend(user_id=1, category='electronics')
    assert len(recs) > 0
    assert all(score <= 1.0 for _, score in recs)

def test_ncf_model_load():
    model = load_ncf_model()
    assert model is not None
    assert model.trainable_weights > 0
```

### Integration Tests
```python
def test_full_recommendation_flow():
    # Load data
    interactions, products, users = load_data()
    
    # Get recommendations
    recs = hybrid_recommend(user_id=1, category='appliances')
    
    # Verify
    assert all(p in products['product_id'] for p, _ in recs)
```

### Performance Tests
```python
def test_recommendation_latency():
    start = time.time()
    hybrid_recommend(user_id=1, category='appliances', n_recommendations=10)
    elapsed = time.time() - start
    
    assert elapsed < 0.01  # Should be < 10ms
```

---

## Monitoring & Observability

### Metrics to Track

```python
{
    'recommendation_latency_ms': <4,  # Average latency
    'cache_hit_rate': 0.95,          # Cache effectiveness
    'model_accuracy': 0.098,          # Hit Rate@10
    'user_coverage': 0.95,            # % users with recommendations
    'product_coverage': 0.85,         # % products recommended
    'error_rate': 0.001,              # Fraction of failed requests
}
```

### Logging

```python
import logging

logger = logging.getLogger(__name__)

logger.info(f"Recommendation for user {user_id}: {len(recs)} results in {latency}ms")
logger.warning(f"Slow recommendation: {latency}ms > threshold")
logger.error(f"Failed to load model: {error}")
```

---

## Future Improvements

### Short Term (v1.1)
- [ ] Advanced embedding techniques (attention mechanisms)
- [ ] Real-time user preference updates
- [ ] Price-based filtering
- [ ] A/B testing framework

### Long Term (v2.0)
- [ ] Multi-armed bandit for exploration/exploitation
- [ ] Context-aware recommendations
- [ ] Temporal dynamics (seasonality)
- [ ] Cross-domain recommendations

---

**See README.md for usage examples and docs/SETUP.md for installation.**

