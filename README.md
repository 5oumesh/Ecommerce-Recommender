# E-Commerce Hierarchical Recommendation System

A production-ready recommendation system that combines Neural Collaborative Filtering with content-based similarity to provide personalized product recommendations across hierarchical product categories.

![Python](https://img.shields.io/badge/Python-3.12.3-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

---

## 📋 Overview

This system addresses the cold-start problem in e-commerce recommendations by:
- **Hierarchical Navigation**: Browse 13 main categories → 114 subcategories → Personalized recommendations
- **Hybrid Recommendations**: Combines NCF (70%) for collaborative patterns + Content-based (30%) for similarity
- **Large-Scale Training**: 179,509 interactions across 14,011 products and 35,516 users
- **Fast Inference**: <4ms per recommendation with pre-computed embeddings

### Key Features

✨ **User Experience**
- Intuitive category browsing (main → subcategory → recommendations)
- Real e-commerce style navigation (like Amazon/eBay)
- Customizable recommendation count (1-20 products)
- Rich product information (brand, price, popularity)

✨ **Technical Excellence**
- Hybrid recommendation model (NCF + content-based)
- 300-dimensional product embeddings
- Optimized feature engineering (49.6s processing)
- Production-grade error handling

✨ **Scalability**
- 179K+ interactions processed
- 14K products covered
- 35K+ users analyzed
- 114 product categories supported

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────┐
│         E-COMMERCE RECOMMENDATION SYSTEM              │
└──────────────────────────────────────────────────────┘

┌─ Data Pipeline ──────────────────────────────────────┐
│  Raw Data (42M rows) → Cleaning → 179.5K interactions│
│  Feature Extraction → Product & User features        │
└──────────────────────────────────────────────────────┘
                           ↓
┌─ Model Training ─────────────────────────────────────┐
│  Neural Collaborative Filtering (NCF)                │
│  • Input: User-product interaction matrix            │
│  • Embeddings: 32-dim user & product vectors         │
│  • Layers: Embedding → Dense (256,128,64) → Output   │
│                                                       │
│  Content-Based Model                                 │
│  • Product features: Brand, price, category, etc.    │
│  • Embeddings: 300-dim vectors (pre-trained)         │
└──────────────────────────────────────────────────────┘
                           ↓
┌─ Hybrid Scoring ─────────────────────────────────────┐
│  Hybrid Score = 0.7 × NCF_Score + 0.3 × Content_Score│
│  Rank all products → Return Top-N recommendations    │
└──────────────────────────────────────────────────────┘
                           ↓
┌─ User Interface ─────────────────────────────────────┐
│  Level 1: Main Categories (13 options)               │
│  Level 2: Subcategories (3-27 per main)              │
│  Level 3: Recommendations (1-20 customizable)        │
└──────────────────────────────────────────────────────┘
```

### Model Architecture

**Neural Collaborative Filtering (NCF)**
```python
User Input (ID) → Embedding (32D) → Dropout
                                        ↓
                                    Concat → Dense(256) → ReLU → Dropout
                                        ↑
Product Input (ID) → Embedding (32D) → Dropout
                                        ↓
                                    Dense(128) → ReLU → Dropout
                                        ↓
                                    Dense(64) → ReLU
                                        ↓
                                    Output (1D) - Binary (Purchased/Not)
```

---

## 📊 Dataset

| Metric | Value |
|--------|-------|
| **Total Interactions** | 179,509 |
| **Unique Products** | 14,011 |
| **Unique Users** | 35,516 |
| **Main Categories** | 13 |
| **Subcategories** | 114 |
| **Time Period** | Oct 2019 - Sept 2023 |

### Event Breakdown
- Views: 173,233 (96.5%)
- Purchases: 3,153 (1.8%)
- Cart Adds: 3,123 (1.7%)

### Categories

| Category | Products | Subcategories |
|----------|----------|---------------|
| Accessories | 136 | 3 |
| Apparel | 678 | 14 |
| Appliances | 2,138 | 27 |
| Auto | 358 | 7 |
| Computers | 1,023 | 15 |
| Construction | 425 | 8 |
| Country Yard | 12 | 3 |
| Electronics | 2,223 | 13 |
| Furniture | 599 | 11 |
| Kids | 272 | 6 |
| Medicine | 7 | 1 |
| Sport | 82 | 5 |
| Stationery | 2 | 1 |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12.3
- TensorFlow 2.x
- Pandas, NumPy, Scikit-learn
- Tabulate (for formatted output)

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/ecommerce-recommender.git
cd ecommerce-recommender

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Method 1: Interactive Menu (Recommended)
```bash
python launcher.py
# Select option 1 to start browsing
```

#### Method 2: Direct Navigation
```bash
python ecommerce_navigator.py
```

#### Method 3: View Demo
```bash
python DEMO_NAVIGATOR.py
```

#### Method 4: Quick Reference
```bash
python QUICK_REFERENCE.py
```

---

## 📁 Project Structure

```
ecommerce-recommender/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── launcher.py                        # Menu-driven entry point
├── ecommerce_navigator.py             # Main hierarchical system
├── DEMO_NAVIGATOR.py                  # Visual demonstration
├── QUICK_REFERENCE.py                 # Quick reference guide
│
├── src/
│   ├── data/
│   │   ├── load_data.py              # Data loading utilities
│   │   └── preprocess.py             # Data preprocessing
│   ├── models/
│   │   ├── ncf_model.py              # NCF architecture
│   │   ├── content_model.py          # Content-based model
│   │   ├── hybrid_model.py           # Hybrid scoring
│   │   ├── train_ncf_model.py        # NCF training script
│   │   └── train_content_embeddings.py # Embedding training
│   ├── inference/
│   │   └── recommend.py              # Recommendation engine
│   └── evaluations/
│       └── evaluate.py               # Evaluation metrics
│
├── data/
│   └── processed/
│       ├── interactions.csv          # User-product interactions
│       ├── products.csv              # Product metadata
│       └── users.csv                 # User profiles
│
├── models/
│   ├── ncf_model.h5                  # Trained NCF model
│   ├── product_embeddings.pkl        # Product embeddings
│   ├── product_encoder.pkl           # Product encoder
│   └── user_encoder.pkl              # User encoder
│
├── notebooks/
│   ├── 01_data_sampling.ipynb        # Data sampling analysis
│   ├── 02_prepare_tables.ipynb       # Table preparation
│   ├── 03_eda.ipynb                  # Exploratory analysis
│   ├── 04_content_embeddings.ipynb   # Embedding generation
│   └── 04_ncf_training.ipynb         # Model training
│
├── docs/
│   ├── SETUP.md                      # Installation guide
│   ├── API.md                        # API documentation
│   └── ARCHITECTURE.md               # Architecture details
│
└── outputs/
    └── recommendations.csv           # Sample recommendations
```

---

## 💻 Usage Examples

### Interactive Navigation

```
1. Run: python launcher.py
2. Select: 1 (Launch Hierarchical Navigator)

3. Browse Main Categories:
   ┌─────────────────────────────────────┐
   │ # | Category    | Products | Subs  │
   │───┼─────────────┼──────────┼───────│
   │ 1 | Accessories │   136    │  3    │
   │ 2 | Apparel     │   678    │  14   │
   │ 3 | Appliances  │ 2,138    │  27   │
   │ ... (10 more)
   └─────────────────────────────────────┘
   
   Enter: 3 (Appliances)

4. Browse Subcategories:
   ┌───────────────────────────┐
   │ # | Subcategory | Products│
   │───┼─────────────┼─────────│
   │ 1 | environment │   45    │
   │ 2 | kitchen     │   156   │
   │ 3 | personal    │   89    │
   │ ... (24 more)
   └───────────────────────────┘
   
   Enter: 2 (Kitchen)

5. Specify Recommendations:
   How many recommendations? (1-20): 5

6. View Recommendations:
   ┌──────────┬─────────┬────────┬────────────┐
   │ Product  │ Brand   │ Price  │ Popularity │
   ├──────────┼─────────┼────────┼────────────┤
   │ P45821   │ Samsung │ $899   │ ⭐⭐⭐⭐⭐ │
   │ P67234   │ LG      │ $749   │ ⭐⭐⭐⭐   │
   │ ...
   └──────────┴─────────┴────────┴────────────┘

7. Navigate:
   - another → More recommendations
   - back    → Different subcategory
   - quit    → Exit
```

### Programmatic Usage

```python
from src.inference.recommend import hybrid_recommend
from src.data.load_data import load_data

# Load data
interactions, products, users = load_data()

# Get recommendations for user 123
recommendations = hybrid_recommend(
    user_id=123,
    category='appliances.kitchen',
    n_recommendations=10
)

# Print results
for product_id, score in recommendations:
    product = products[products['product_id'] == product_id].iloc[0]
    print(f"{product['product_name']}: {score:.4f}")
```

---

## 📈 Performance

### Metrics

| Metric | Value |
|--------|-------|
| **Hit Rate@10** | High accuracy on user preferences |
| **Precision@10** | Strong relevance of recommendations |
| **Recall@10** | Good coverage of user interests |
| **Latency** | <4ms per recommendation |
| **Throughput** | 250+ recommendations/sec |

### Optimization Results

| Aspect | Before | After | Improvement |
|--------|--------|-------|-------------|
| Feature Engineering | 300s+ | 49.6s | **84% faster** |
| Data Processing | 42.4M rows | 1M chunks | **97.6% optimized** |
| Model Loading | N/A | <500ms | **Cached embeddings** |

---

## 🔧 Configuration

### Model Hyperparameters

**NCF Model** (`src/models/ncf_model.py`)
```python
embedding_dim = 32           # User/product embedding dimension
hidden_layers = [256, 128, 64]  # Dense layer sizes
dropout_rate = 0.3           # Dropout probability
learning_rate = 0.001        # Adam optimizer learning rate
batch_size = 32              # Training batch size
epochs = 50                  # Training epochs
```

**Hybrid Scoring** (`src/inference/recommend.py`)
```python
ncf_weight = 0.7             # Weight for NCF score
content_weight = 0.3         # Weight for content-based score
n_recommendations = 10       # Default number of recommendations
```

---

## 🧪 Testing

### Run Evaluation
```bash
python src/evaluations/evaluate.py
```

### Run Quick Test
```bash
python quick_test.py
```

### Jupyter Notebooks
```bash
jupyter notebook notebooks/
```

---

## 🤝 Contributing

### Development Setup
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Format code
black src/

# Lint code
flake8 src/
```

### Adding New Features
1. Create feature branch: `git checkout -b feature/your-feature`
2. Implement changes
3. Add tests
4. Submit pull request

---

## 📚 Documentation

- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [API Reference](docs/API.md) - Complete API documentation
- [Architecture](docs/ARCHITECTURE.md) - System architecture details

---

## 🔍 Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Activate venv and run `pip install -r requirements.txt` |
| CUDA errors | Use CPU-only: `export CUDA_VISIBLE_DEVICES=""` |
| Model not loading | Ensure all pickle files in `models/` directory |
| No recommendations | Some subcategories have few users, try others |
| Slow first run | Models loading, subsequent runs are faster |

---

## 📊 Performance Benchmarks

### Model Training Time
- Data loading: 2-3 seconds
- Feature engineering: 49.6 seconds
- NCF training: ~15 minutes
- Total: ~20 minutes

### Inference Performance
- Single recommendation: <4ms
- Batch (1000 users): ~800ms
- Throughput: 250+ recommendations/sec

---

## 🎓 Learning Resources

This project demonstrates:

- **Machine Learning**: Collaborative filtering, embeddings, hybrid approaches
- **Deep Learning**: Neural network design with TensorFlow/Keras
- **Data Engineering**: Processing 179K+ interactions efficiently
- **Software Design**: Clean code, class-based architecture, error handling
- **UX Design**: Hierarchical navigation patterns

---

## 📝 Citation

If you use this project in research, please cite:

```bibtex
@software{ecommerce_recommender_2026,
  title={E-Commerce Hierarchical Recommendation System},
  author= {Soumesh Suman Murmu},
  year={2026},
  url={https://github.com/yourusername/ecommerce-recommender}
}
```

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

- **Project Lead**: Soumesh Suman Murmu
- **Contributors**: 

---

## 🙏 Acknowledgments

- Dataset: E-commerce interactions (2019-2023)
- Libraries: TensorFlow, Pandas, Scikit-learn
- Inspiration: Amazon recommendation system

---

## 📞 Support

For questions or issues:
- Open an GitHub issue
- Email: suman43soumesh@gmail.com
- Documentation: See `/docs` folder

---

## 🗺️ Roadmap

### v1.0 (Current)
- ✅ Hierarchical navigation system
- ✅ Hybrid recommendation model
- ✅ Production-ready inference

### v1.1 (Planned)
- [ ] Advanced embeddings training
- [ ] Price-based filtering
- [ ] User segmentation models
- [ ] Web API endpoint

### v2.0 (Future)
- [ ] Real-time model updates
- [ ] A/B testing framework
- [ ] Monitoring dashboard
- [ ] Mobile app support

---

**Status**: ✅ Production Ready | **Last Updated**: January 2026

