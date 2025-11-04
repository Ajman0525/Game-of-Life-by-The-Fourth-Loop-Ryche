import copy
from src.next_generation import next_generation

def test_underpopulation():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    new_grid = next_generation(grid)
    assert new_grid[1][1] == 0, "A lone live cell should die (underpopulation)."

def test_survival():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    new_grid = next_generation(grid)
    assert new_grid[1][1] == 1, "A live cell with 2 or 3 neighbors should survive."

def test_overpopulation():
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 0, 0],
    ]
    new_grid = next_generation(grid)
    assert new_grid[1][1] == 0, "A live cell with >3 neighbors should die (overpopulation)."

def test_reproduction():
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 0, 0],
    ]
    new_grid = next_generation(grid)
    assert new_grid[1][1] == 1, "A dead cell with exactly 3 neighbors should become alive."

def test_dimensions_unchanged():
    grid = [
        [0, 1],
        [1, 0]
    ]
    new_grid = next_generation(grid)
    assert len(grid) == len(new_grid) and len(grid[0]) == len(new_grid[0]), \
        "Grid dimensions must remain the same."

def test_immutability():
    grid = [
        [1, 0],
        [0, 1]
    ]
    grid_copy = copy.deepcopy(grid)
    _ = next_generation(grid)
    assert grid == grid_copy, "Original grid must not be mutated."
