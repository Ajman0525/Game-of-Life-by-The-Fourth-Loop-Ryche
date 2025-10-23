import pytest
from src.multiple_generation import multiple_generation  

# Sample grid
@pytest.fixture
def grid():
    return [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]

# Number of generations
@pytest.fixture
def number_of_generations():
    return 3  # can be overridden per test

# Simulating multiple generations
def test_multiple_generation(grid, number_of_generations):
    """
    Simulate the Game of Life for `number_of_generations` generations.
    Should return a new grid without modifying the original.
    """
    result = multiple_generation(grid, number_of_generations)
    
    # At this stage, we just check the output is a list of lists with same dimensions
    assert isinstance(result, list)
    assert all(isinstance(row, list) for row in result)
    assert len(result) == len(grid)
    assert all(len(row) == len(grid[0]) for row in result)

# Test: simulating zero generations
def test_zero_generation(grid):
    """
    Simulating 0 generations returns the original grid unchanged.
    """
    result = multiple_generation(grid, 0)
    assert result == grid  # should match exactly
