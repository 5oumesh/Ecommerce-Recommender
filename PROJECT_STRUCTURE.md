# Project Structure Overview

## GitHub-Ready Repository Structure

```
ecommerce-recommender/
│
├── 📄 README.md                          # Main project documentation
├── 📄 requirements.txt                   # Python dependencies
├── 📄 LICENSE                            # MIT License
├── 📄 .gitignore                         # Git ignore rules
│
├── 🎯 Entry Points (User-Facing)
│   ├── launcher.py                       # Menu-driven interface (START HERE)
│   ├── ecommerce_navigator.py            # Main hierarchical navigation system
│   ├── DEMO_NAVIGATOR.py                 # Visual demonstration
│   └── QUICK_REFERENCE.py                # Quick reference guide
│
├── 📁 src/                               # Source Code
│   ├── __init__.py
│   │
│   ├── 📂 data/                          # Data Loading & Processing
│   │   ├── __init__.py
│   │   ├── load_data.py                  # Load CSV files into memory
│   │   └── preprocess.py                 # Data cleaning & validation
│   │
│   ├── 📂 models/                        # Model Implementations
│   │   ├── __init__.py
│   │   ├── ncf_model.py                  # Neural Collaborative Filtering
│   │   ├── content_model.py              # Content-based similarity model
│   │   ├── hybrid_model.py               # Hybrid recommendation logic
│   │   ├── train_ncf_model.py            # NCF training script
│   │   └── train_content_embeddings.py   # Embedding training
│   │
│   ├── 📂 inference/                     # Recommendation Engine
│   │   ├── __init__.py
│   │   └── recommend.py                  # hybrid_recommend() main function
│   │
│   └── 📂 evaluations/                   # Model Evaluation
│       ├── __init__.py
│       ├── evaluate.py                   # Metric calculations
│       ├── comparison_report.py          # Model comparison
│       ├── detailed_report.py            # Detailed analysis
│       └── metrics_guide.py              # Metric explanations
│
├── 📁 data/                              # Dataset
│   └── processed/                        # Cleaned & processed data
│       ├── interactions.csv              # 179,509 user-product interactions
│       ├── products.csv                  # 14,011 product metadata
│       ├── products_enriched.csv         # Products with features
│       ├── users.csv                     # 35,516 user profiles
│       └── users_enriched.csv            # Users with aggregated features
│
├── 📁 models/                            # Trained Models & Embeddings
│   ├── ncf_model.h5                      # Neural Collaborative Filtering (TensorFlow)
│   ├── product_embeddings.pkl            # 14K product embeddings (300D)
│   ├── product_encoder.pkl               # Product ID encoder
│   └── user_encoder.pkl                  # User ID encoder
│
├── 📁 notebooks/                         # Jupyter Analysis Notebooks
│   ├── 01_data_sampling.ipynb            # Data sampling & exploration
│   ├── 02_prepare_tables.ipynb           # Table preparation & merging
│   ├── 03_eda.ipynb                      # Exploratory Data Analysis
│   ├── 04_content_embeddings.ipynb       # Embedding generation
│   └── 04_ncf_training.ipynb             # NCF model training
│
├── 📁 docs/                              # Documentation
│   ├── SETUP.md                          # Installation & setup guide
│   ├── API.md                            # API reference & examples
│   └── ARCHITECTURE.md                   # System architecture details
│
└── 📁 outputs/                           # Generated Files (optional)
    └── recommendations.csv               # Sample recommendations
```

---

## Quick Navigation

### For Users
- **Start Here**: `launcher.py` (menu-driven interface)
- **Direct Access**: `ecommerce_navigator.py` (hierarchical navigator)
- **Learn**: `DEMO_NAVIGATOR.py` (visual examples)
- **Reference**: `QUICK_REFERENCE.py` (quick guide)

### For Developers
- **Entry Points**: `src/inference/recommend.py` (main recommendation function)
- **Data Loading**: `src/data/load_data.py` (CSV loading)
- **Models**: `src/models/` (NCF, content-based, hybrid implementations)
- **Training**: `notebooks/` (Jupyter notebooks for retraining)

### For Documentation
- **Overview**: `README.md` (project overview)
- **Installation**: `docs/SETUP.md` (setup guide)
- **API Reference**: `docs/API.md` (function documentation)
- **Architecture**: `docs/ARCHITECTURE.md` (system design)

---

## File Descriptions

### Root Files

| File | Purpose | Type |
|------|---------|------|
| `README.md` | Main project documentation | Documentation |
| `requirements.txt` | Python dependencies | Config |
| `LICENSE` | MIT License | Legal |
| `.gitignore` | Git ignore rules | Config |

### Entry Points (4 files)

| File | Purpose | When to Use |
|------|---------|------------|
| `launcher.py` | Menu-driven interface | First-time users |
| `ecommerce_navigator.py` | Direct hierarchical navigator | Power users |
| `DEMO_NAVIGATOR.py` | Visual demonstration | Learning |
| `QUICK_REFERENCE.py` | Quick reference guide | Quick lookup |

### Source Code (src/ - 12 files)

**Data Module** (2 files)
- `load_data.py` - Load CSV files
- `preprocess.py` - Clean & validate data

**Models Module** (5 files)
- `ncf_model.py` - Neural Collaborative Filtering
- `content_model.py` - Content-based similarity
- `hybrid_model.py` - Hybrid combination
- `train_ncf_model.py` - Training script
- `train_content_embeddings.py` - Embedding training

**Inference Module** (1 file)
- `recommend.py` - Main recommendation engine

**Evaluation Module** (4 files)
- `evaluate.py` - Metric calculations
- `comparison_report.py` - Model comparison
- `detailed_report.py` - Analysis report
- `metrics_guide.py` - Metric explanations

### Data (data/processed/ - 5 CSV files)

| File | Rows | Columns | Purpose |
|------|------|---------|---------|
| `interactions.csv` | 179,509 | 5 | User-product interactions |
| `products.csv` | 14,011 | 6 | Product metadata |
| `products_enriched.csv` | 14,011 | 12 | Products + features |
| `users.csv` | 35,516 | 4 | User profiles |
| `users_enriched.csv` | 35,516 | 8 | Users + aggregated features |

### Models (models/ - 4 files)

| File | Size | Purpose |
|------|------|---------|
| `ncf_model.h5` | ~2.6 MB | Trained NCF model |
| `product_embeddings.pkl` | ~2.7 MB | 14K product embeddings (300D) |
| `product_encoder.pkl` | ~0.02 MB | Product ID encoder |
| `user_encoder.pkl` | ~0.01 MB | User ID encoder |

### Notebooks (notebooks/ - 5 files)

| File | Purpose | Execution Time |
|------|---------|-----------------|
| `01_data_sampling.ipynb` | Sampling exploration | ~2 minutes |
| `02_prepare_tables.ipynb` | Table preparation | ~1 minute |
| `03_eda.ipynb` | Statistical analysis | ~3 minutes |
| `04_content_embeddings.ipynb` | Embedding generation | ~5 minutes |
| `04_ncf_training.ipynb` | Model training | ~15 minutes |

### Documentation (docs/ - 3 files)

| File | Purpose | Audience |
|------|---------|----------|
| `SETUP.md` | Installation guide | Everyone |
| `API.md` | Function reference | Developers |
| `ARCHITECTURE.md` | System design | Architects |

---

## Data Specifications

### interactions.csv
```
user_id (int)
product_id (str)
event_type (str) - 'view', 'purchase', 'cart_add'
price (float)
timestamp (datetime)
```

### products.csv
```
product_id (str)
name (str)
brand (str)
price (float)
category (str) - Format: 'main.subcategory'
url (str)
```

### users.csv
```
user_id (int)
total_interactions (int)
total_purchases (int)
favorite_category (str)
```

---

## Model Specifications

### NCF Model (ncf_model.h5)
- **Architecture**: 3-layer MLP with embeddings
- **Input**: User ID + Product ID (separate streams)
- **Embeddings**: 32D for users, 32D for products
- **Hidden Layers**: [256, 128, 64]
- **Output**: Binary (purchased/not purchased)
- **Size**: ~2.6 MB

### Product Embeddings (product_embeddings.pkl)
- **Format**: Dictionary {product_id: embedding_vector}
- **Dimension**: 300D vectors
- **Generation**: Content-based feature aggregation
- **Total**: 14,011 embeddings
- **Size**: ~2.7 MB

---

## File Count Summary

| Category | Count | Total Size |
|----------|-------|-----------|
| Python Scripts | 4 | ~50 KB |
| Source Modules | 12 | ~100 KB |
| Jupyter Notebooks | 5 | ~2 MB |
| Data Files | 5 | ~50 MB |
| Model Files | 4 | ~5.3 MB |
| Documentation | 4 | ~200 KB |
| **TOTAL** | **34** | **~57.5 MB** |

---

## GitHub Upload Checklist

- ✅ Clean folder structure
- ✅ No unnecessary files (removed interim/, raw data, etc.)
- ✅ Python package structure (__init__.py files)
- ✅ Comprehensive README.md
- ✅ API documentation
- ✅ Installation guide
- ✅ Architecture documentation
- ✅ requirements.txt
- ✅ .gitignore
- ✅ LICENSE
- ✅ Sample notebooks for learning
- ✅ Example recommendation output

**Ready for GitHub upload! 🚀**

---

## How to Use This Structure

### Clone & Setup
```bash
git clone <repo-url>
cd ecommerce-recommender
pip install -r requirements.txt
python launcher.py
```

### Explore
```bash
# Try the main system
python ecommerce_navigator.py

# See a demo
python DEMO_NAVIGATOR.py

# Run notebooks
jupyter notebook notebooks/
```

### Develop
```bash
# Modify models
vim src/models/ncf_model.py

# Retrain
python src/models/train_ncf_model.py

# Evaluate
python src/evaluations/evaluate.py
```

---

*This structure is GitHub-ready and can be pushed immediately.*

