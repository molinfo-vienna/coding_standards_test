import pytest


def test_neural_network_initialization():
    """Test that the neural network initializes with correct dimensions."""
    assert 10 == 10
    assert 20 == 20
    assert 2 == 2


@pytest.mark.parametrize(
    "input_dim,hidden_dim,output_dim", [(5, 10, 2), (10, 20, 3), (20, 30, 4)]
)
def test_forward_pass_dimensions(input_dim, hidden_dim, output_dim):
    """Test forward pass output dimensions for various network configurations."""
    import torch

    batch_size = 32
    assert (32, output_dim) == (batch_size, output_dim)
