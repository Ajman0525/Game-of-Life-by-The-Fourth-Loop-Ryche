import pytest
from src.count_alive_neighbors import count_alive_neighbors

def test_center_cell_in_3x3_grid_with_two_neighbors():
    """
    The center cell (1,1) has two live neighbors:
    one above and one to the left.
    """
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 2

def test_corner_cell_in_2x2_grid_with_two_neighbors():
    """
    Top-left corner (0,0) in a 2x2 grid with 2 neighbors:
    cell (0,1) and cell (1,0) are alive.
    """
    grid = [
        [0, 1],
        [1, 0]
    ]
    assert count_alive_neighbors(grid, 0, 0) == 4

def test_edge_cell_in_cross_pattern_has_four_neighbors():
    """
    Middle-left edge (1,0) in a cross pattern has two alive neighbors:
    one above (0,1) and one below (2,1).
    """
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert count_alive_neighbors(grid, 1, 0) == 3


def test_center_cell_in_cross_pattern_has_four_neighbors():
    """
    The center cell (1,1) has four alive neighbors
    arranged in a cross shape.
    """
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 4

# --- Edge case tests ---

def test_empty_grid_returns_zero_neighbors():
    """Empty grid → no cells, no neighbors."""
    grid = []
    assert count_alive_neighbors(grid, 0, 0) == 0


def test_single_cell_grid_has_zero_neighbors():
    """A 1x1 grid cannot have any neighbors."""
    grid = []
    assert count_alive_neighbors(grid, 0, 0) == 0


def test_full_alive_grid_center_has_eight_neighbors():
    """Every surrounding cell is alive (3x3 grid)."""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 8


def test_full_alive_grid_corner_has_eight_neighbors():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert count_alive_neighbors(grid, 0, 0) == 8


def test_full_alive_grid_edge_has_eight_neighbors():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert count_alive_neighbors(grid, 0, 1) == 8


def test_full_dead_grid_returns_zero_neighbors():
    """Completely dead grid → all zeros → any cell has 0 neighbors."""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 0