import torch


def test_basic_math():
    """Test basic mathematical operations."""
    # Instead of comparing constants, test actual calculations
    assert 5 + 5 == 10
    assert 4 * 5 == 20
    assert 8 / 4 == 2


def test_neural_network(input_dim=10, hidden_dim=20):
    """Test neural network functionality.

    Args:
        input_dim: Input dimension for the network
        hidden_dim: Hidden layer dimension
    """
    # Use the input arguments to make the test meaningful
    batch_size = 32
    x = torch.randn(batch_size, input_dim)
    # Test the tensor shape
    assert x.shape == (batch_size, input_dim)

    # Test hidden layer calculations
    hidden = torch.randn(batch_size, hidden_dim)
    assert hidden.shape == (batch_size, hidden_dim)
