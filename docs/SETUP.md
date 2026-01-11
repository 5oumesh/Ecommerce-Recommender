# Installation & Setup Guide

## System Requirements

- **OS**: Linux, macOS, or Windows
- **Python**: 3.10 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB (for data + models)

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ecommerce-recommender.git
cd ecommerce-recommender
```

### 2. Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import tensorflow; import pandas; import numpy; print('✅ All dependencies installed')"
```

## Dependencies

### Core Libraries
- **TensorFlow 2.x** - Deep learning framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning utilities
- **Tabulate** - Formatted table display

### Development (Optional)
- **Jupyter** - Interactive notebooks
- **Pytest** - Testing framework
- **Black** - Code formatting
- **Flake8** - Code linting

## Troubleshooting

### TensorFlow Installation Issues

**Issue**: CUDA/GPU related errors
```bash
# Use CPU-only version
pip install tensorflow-cpu
```

**Issue**: Memory errors during training
```bash
# Reduce batch size in config
# Edit: src/models/train_ncf_model.py
# Change: batch_size = 16  # (reduce from 32)
```

### Data Loading Issues

**Issue**: "File not found" error
```bash
# Ensure you're in correct directory
pwd  # Check current directory
ls data/processed/  # Verify data files exist
```

**Issue**: CSV encoding problems
```python
# Use encoding parameter
pd.read_csv('path/to/file.csv', encoding='utf-8')
```

### Model Loading Issues

**Issue**: Pickle files corrupted
```bash
# Re-download models from releases
# Or retrain using notebooks
```

**Issue**: TensorFlow version mismatch
```bash
# Check version
python -c "import tensorflow; print(tensorflow.__version__)"

# Update if needed
pip install --upgrade tensorflow
```

## Environment Variables

### Optional Configuration

```bash
# Use CPU only (if GPU causes issues)
export CUDA_VISIBLE_DEVICES=""

# Set memory limit (if running on low RAM)
export TF_CPP_MIN_LOG_LEVEL=2
```

## Docker Setup (Optional)

### Build Docker Image
```bash
docker build -t ecommerce-recommender .
```

### Run Container
```bash
docker run -it ecommerce-recommender
python launcher.py
```

## Development Setup

### Install Dev Dependencies
```bash
pip install -r requirements-dev.txt
```

### Setup Pre-commit Hooks
```bash
pre-commit install
```

### Run Tests
```bash
pytest tests/ -v
```

## Next Steps

1. **Verify Installation**: `python launcher.py`
2. **Run Demo**: `python DEMO_NAVIGATOR.py`
3. **Check Notebooks**: `jupyter notebook notebooks/`
4. **Read API Docs**: See `docs/API.md`

---

For issues, see README.md troubleshooting section.

