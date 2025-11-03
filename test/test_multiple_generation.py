from src.multiple_generation import multiple_generation

def test_zero_generation():
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
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    expected = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result = multiple_generation(grid, 1)
    assert result == expected


def test_multiple_generations():
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    gen1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    gen2 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    result = multiple_generation(grid, 3)
    assert result == expected


def test_grid_dimensions_remain_consistent():
    grid = [
        [1, 0],
        [0, 1]
    ]
    result = multiple_generation(grid, 5)
    assert len(result) == len(grid)
    assert all(len(row) == len(grid[0]) for row in result)


def test_static_grid_remains_static():
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
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    original_copy = [row[:] for row in grid]
    multiple_generation(grid, 2)
    assert grid == original_copy
