from src.multiple_generation import multiple_generation

def test_zero_generation():
    """Simulating 0 generations should return the same grid (no evolution)."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    expected = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = multiple_generation(grid, 0)
    assert result == expected


def test_one_generation():
    """After 1 generation, the grid evolves according to Conway's rules."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Expected after one generation (manually reasoned)
    expected = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result = multiple_generation(grid, 1)
    assert result == expected


def test_multiple_generations():
    """Simulate multiple generations and verify the final outcome."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Let's simulate 3 generations manually
    # Generation 1
    gen1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Generation 2 → same as gen1 (becomes static)
    gen2 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Generation 3 → still static
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    result = multiple_generation(grid, 3)
    assert result == expected


def test_grid_dimensions_remain_consistent():
    """Grid dimensions stay the same after any number of generations."""
    grid = [
        [1, 0],
        [0, 1]
    ]
    result = multiple_generation(grid, 5)
    assert len(result) == len(grid)
    assert all(len(row) == len(grid[0]) for row in result)


def test_static_grid_remains_static():
    """A completely dead grid should remain unchanged forever."""
    grid = [
        [0, 0],
        [0, 0]
    ]
    expected = [
        [0, 0],
        [0, 0]
    ]
    result = multiple_generation(grid, 3)
    assert result == expected


def test_original_grid_not_modified():
    """Ensure that the input grid is not changed during simulation."""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    original_copy = [row[:] for row in grid]
    multiple_generation(grid, 2)
    assert grid == original_copy
