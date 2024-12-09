# Python Package Configuration Guide

## Table of Contents
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration Files](#configuration-files)
- [Dependency Management](#dependency-management)
- [Development Tools](#development-tools)
- [Publishing](#publishing)

## Quick Start

1. **Clone and Install**
```bash
git clone https://github.com/molinfo-vienna/coding_standards_test
cd coding_standards_test
pip install -e ".[dev,viz,docs]"  # Install all dependencies
```

2. **Run Quality Checks**
```bash
pytest                 # Run tests
black .               # Format code
isort .              # Sort imports
pylint src tests     # Check code quality
pydocstyle src       # Check docstrings
mypy src             # Check types
```

## Project Structure

```
your-package/
├── src/
│   └── your_package/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/
│   ├── conf.py
│   └── index.rst
├── .gitignore
├── LICENSE
├── README.md
├── README_PACKAGE.md
└── pyproject.toml
```

## Configuration Files

Modern Python packaging uses `pyproject.toml` as the single source of truth for project configuration. This project uses Hatchling as the build backend.

### Why Hatchling?
Hatchling is a modern, extensible build backend for Python projects that offers several advantages:
- Fast build times through aggressive caching
- Built-in support for common project configurations
- Dynamic version string management
- Simplified dependency specification
- Plugin system for custom build steps
- Better handling of package data and resources
- Native support for Python wheels

Unlike older tools like setuptools, Hatchling is designed specifically for modern Python packaging standards (PEP 517/PEP 518) and doesn't require additional files like setup.py or setup.cfg.

### pyproject.toml

The main configuration file is divided into several sections:

1. **Build System**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

2. **Project Metadata**
```toml
[project]
name = "coding_standards"
version = "0.1.0"
description = "A machine learning package"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
```

3. **Dependencies**
```toml
dependencies = [
    "torch>=2.0.0",
    "torchvision>=0.15.0",
    "scikit-learn>=1.2.0",
    "numpy>=1.24.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
viz = [
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "plotly>=5.13.0",
]
dev = [
    "black>=23.3.0",
    "isort>=5.12.0",
    "pylint>=2.17.0",
    # ... other dev tools
]
docs = [
    "sphinx>=6.0.0",
    "sphinx-rtd-theme>=1.2.0",
]
```

4. **Tool Configurations**
```toml
[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=xml --cov-report=term-missing"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.pylint.messages_control]
disable = [
    "C0111",  # missing-docstring
    "C0103",  # invalid-name
]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
```

### MANIFEST.in
```
include LICENSE
include README.md
include requirements.txt
recursive-include src/package_name/data *
recursive-include docs *.rst
global-exclude *.py[cod]
```

## Dependency Management

### Installation Options

1. **Basic Installation**
```bash
pip install .
```

2. **Development Installation**
```bash
pip install -e ".[dev]"
```

3. **Full Installation**
```bash
pip install -e ".[dev,viz,docs]"
```

### Managing Dependencies

1. **Core Dependencies**: Required for basic functionality
   - PyTorch
   - scikit-learn
   - NumPy
   - pandas

2. **Visualization Dependencies**: Optional for plotting
   - matplotlib
   - seaborn
   - plotly

3. **Development Dependencies**: For contributing
   - black (formatting)
   - isort (import sorting)
   - pylint (linting)
   - pytest (testing)
   - mypy (type checking)

4. **Documentation Dependencies**: For building docs
   - sphinx
   - sphinx-rtd-theme

## Development Tools

### Code Quality

1. **Formatting**
```bash
# Format code
black .

# Sort imports
isort .
```

2. **Linting**
```bash
# Check code quality
pylint src tests

# Check types
mypy src

# Check docstrings
pydocstyle src
```

3. **Testing**
```bash
# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_core.py
```

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
-   repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    -   id: black
-   repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    -   id: isort
```

## Publishing

### 1. Build Package
```bash
python -m build
```

### 2. Check Package
```bash
twine check dist/*
```

### 3. Upload to PyPI
```bash
# Upload to test PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Upload to PyPI
twine upload dist/*
```

### Required Files for PyPI
The modern Python packaging system requires only:
- `pyproject.toml` (package configuration and build settings)
- Source code in `src/`
- `README.md` (project documentation)
- `LICENSE` (project license)

## Best Practices

1. **Version Management**
   - Use semantic versioning (MAJOR.MINOR.PATCH)
   - Keep CHANGELOG.md updated

2. **Documentation**
   - Write comprehensive docstrings
   - Include usage examples
   - Keep README updated
   - Generate API documentation

3. **Testing**
   - Write unit tests (pytest)
   - Maintain high coverage
   - Include integration tests
   - Test all supported Python versions

4. **Code Quality**
   - Follow PEP 8 style guide
   - Use type hints
   - Write clear docstrings
   - Keep functions focused and simple

5. **Git Workflow**
   - Use meaningful commit messages
   - Create feature branches
   - Submit pull requests
   - Review code changes