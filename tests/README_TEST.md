# Testing Guide

## Table of Contents 
- [Overview](#overview)
- [Test Structure](#test-structure)
- [Writing Tests](#writing-tests)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [Best Practices](#best-practices)
- [Examples](#examples)

## Overview

This project uses pytest for unit testing. Tests are organized in the 'tests/' directory, mirroring the structure of the source code in 'src/'.

### Testing Tools
- **pytest**: Main testing framework
- **pytest-cov**: Coverage reporting
- **pytest-mock**: Mocking functionality
- **pytest-xdist**: Parallel test execution

## Test Structure

```python
tests/
├── __init__.py
├── test_stuff.py                 # Shared fixtures
├── test_core/
│   ├── __init__.py
│   ├── test_model.py          # Tests for model.py
│   └── test_training.py       # Tests for training.py
├── test_utils/
│   ├── __init__.py
│   ├── test_data_loading.py   # Tests for data_loading.py
│   └── test_preprocessing.py  # Tests for preprocessing.py
└── test_integration/
    ├── __init__.py
    └── test_pipeline.py       # End-to-end tests
```

## Writing Tests

### Basic Test Structure
```python
# test_model.py
import pytest
from your_package.core.model import NeuralNetwork

def test_neural_network_initialization():
    """Test that the neural network initializes with correct dimensions."""
    model = NeuralNetwork(input_dim=10, hidden_dim=20, output_dim=2)
    assert model.input_dim == 10
    assert model.hidden_dim == 20
    assert model.output_dim == 2

@pytest.mark.parametrize("input_dim,hidden_dim,output_dim", [
    (5, 10, 2),
    (10, 20, 3),
    (20, 30, 4)
])
def test_forward_pass_dimensions(input_dim, hidden_dim, output_dim):
    """Test forward pass output dimensions for various network configurations."""
    import torch
    model = NeuralNetwork(input_dim, hidden_dim, output_dim)
    batch_size = 32
    x = torch.randn(batch_size, input_dim)
    output = model(x)
    assert output.shape == (batch_size, output_dim)

@pytest.fixture
def sample_model():
    """Fixture providing a pre-configured model for tests."""
    model = NeuralNetwork(input_dim=10, hidden_dim=20, output_dim=2)
    return model

def test_model_training(sample_model):
    """Test model training for one epoch."""
    # Test implementation
    pass

def test_model_raises_value_error():
    """Test that model raises ValueError for invalid dimensions."""
    with pytest.raises(ValueError):
        NeuralNetwork(input_dim=-1, hidden_dim=20, output_dim=2)
```

### Using Fixtures (conftest.py)
```python
# conftest.py
import pytest
import torch
import numpy as np

@pytest.fixture(scope="session")
def sample_data():
    """Generate sample data for tests."""
    np.random.seed(42)
    X = np.random.randn(100, 10)
    y = np.random.randint(0, 2, 100)
    return torch.FloatTensor(X), torch.LongTensor(y)

@pytest.fixture(scope="function")
def model_config():
    """Provide model configuration."""
    return {
        "input_dim": 10,
        "hidden_dim": 20,
        "output_dim": 2,
        "learning_rate": 0.01
    }
```

## Running Tests

### Basic Test Execution
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_core/test_model.py

# Run specific test
pytest tests/test_core/test_model.py::test_neural_network_initialization
```

### Advanced Test Execution
```bash
# Run tests in parallel
pytest -n auto

# Run tests with coverage
pytest --cov=src

# Generate HTML coverage report
pytest --cov=src --cov-report=html

# Run tests matching specific pattern
pytest -k "model"

# Show stdout/stderr during test execution
pytest -s

# Show verbose output
pytest -v
```

## Test Coverage

Coverage configuration in pyproject.toml:
```toml
[tool.coverage.run]
source = ["src"]
omit = ["tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "pass",
]
```

### Coverage Targets
- Aim for at least 80% coverage for the entire codebase
- Critical path code should have 100% coverage
- Document any intentionally uncovered code

## Best Practices

1. **Test Organization**
   - One test file per source file
   - Use clear, descriptive test names
   - Group related tests in classes
   - Use fixtures for shared setup

2. **Test Design**
   - Test one thing per test
   - Use descriptive test names
   - Follow Arrange-Act-Assert pattern
   - Test edge cases and error conditions

3. **Assertions**
   - Use specific assertions (e.g., 'assert_almost_equal' for floats)
   - Include meaningful error messages
   - Check for expected exceptions

4. **Mocking**
   - Mock external dependencies
   - Use context managers for temporary changes
   - Keep mocking simple and focused

5. **Performance**
   - Keep tests fast
   - Use appropriate fixture scopes
   - Parallelize test execution when possible

## Examples

### Testing Data Processing
```python
# test_preprocessing.py
import pytest
import numpy as np
from your_package.utils.preprocessing import normalize_data

def test_normalize_data():
    """Test data normalization."""
    # Arrange
    data = np.array([[1, 2], [3, 4]], dtype=np.float32)
    
    # Act
    normalized = normalize_data(data)
    
    # Assert
    assert normalized.mean(axis=0).round(6).tolist() == [0.0, 0.0]
    assert normalized.std(axis=0).round(6).tolist() == [1.0, 1.0]
```

### Testing Model Components
```python
# test_layers.py
import pytest
import torch
from your_package.core.layers import AttentionLayer

@pytest.mark.parametrize("batch_size,seq_len,hidden_dim", [
    (32, 10, 64),
    (16, 20, 128),
])
def test_attention_layer_output_shape(batch_size, seq_len, hidden_dim):
    """Test attention layer output dimensions."""
    # Arrange
    layer = AttentionLayer(hidden_dim)
    x = torch.randn(batch_size, seq_len, hidden_dim)
    
    # Act
    output, weights = layer(x)
    
    # Assert
    assert output.shape == (batch_size, seq_len, hidden_dim)
    assert weights.shape == (batch_size, seq_len, seq_len)
```

### Testing Training Pipeline
```python
# test_pipeline.py
import pytest
import torch
from your_package.core.training import train_model

def test_training_improves_loss(sample_model, sample_data):
    """Test that training reduces loss."""
    # Arrange
    X, y = sample_data
    initial_loss = compute_loss(sample_model, X, y)
    
    # Act
    train_model(sample_model, X, y, epochs=5)
    final_loss = compute_loss(sample_model, X, y)
    
    # Assert
    assert final_loss < initial_loss
```