from src.generation import next_generation
from src.multiple_generation import multiple_generation  # you will implement this

def test_zero_generation():
    """Simulating 0 generations returns the original grid unchanged."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = multiple_generation(grid, 0)
    assert result == grid


def test_one_generation():
    """Simulating 1 generation matches next_generation."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    expected = next_generation(grid)
    result = multiple_generation(grid, 1)
    assert result == expected