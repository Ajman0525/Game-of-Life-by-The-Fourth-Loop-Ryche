from src.next_generation import next_generation
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

def test_multiple_generations():
    """Simulating multiple generations evolves the grid correctly."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    generations = 3
    result = multiple_generation(grid, generations)

    expected = grid
    for _ in range(generations):
        expected = next_generation(expected)

    assert result == expected

def test_grid_dimensions_remain_consistent():
    """Grid dimensions remain the same after simulation."""
    grid = [
        [1, 0],
        [0, 1]
    ]
    result = multiple_generation(grid, 5)
    assert len(result) == len(grid)
    assert all(len(row) == len(grid[0]) for row in result)

def test_static_grid_remains_static():
    """Static grid should remain unchanged."""
    grid = [
        [0, 0],
        [0, 0]
    ]
    result = multiple_generation(grid, 3)
    assert result == grid

def test_original_grid_not_modified():
    """Original grid remains unchanged after simulation."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    original_copy = [row[:] for row in grid]
    multiple_generation(grid, 2)
    assert grid == original_copy
