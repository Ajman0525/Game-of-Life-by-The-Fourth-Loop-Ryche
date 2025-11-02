# test_grid_init.py
from src.grid_init import Grid

def test_grid_creation():
    data = [
        [1, 0, 0],
        [0, 1, 1],
        [1, 0, 1]
    ]
    grid = Grid(data=data)
    assert grid.rows == 3
    assert grid.cols == 3
    assert grid.get_grid() == data
