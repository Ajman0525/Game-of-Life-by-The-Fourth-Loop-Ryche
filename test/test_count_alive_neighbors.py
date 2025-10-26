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
    assert count_alive_neighbors(grid, 0, 0) == 2

def test_edge_cell_in_cross_pattern_has_two_neighbors():
    """
    Middle-left edge (1,0) in a cross pattern has two alive neighbors:
    one above (0,1) and one below (2,1).
    """
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert count_alive_neighbors(grid, 1, 0) == 2


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

def test_out_of_bounds_returns_zero():
    """
    If the coordinates are outside the grid boundaries,
    function should return 0 safely.
    """
    grid = [
        [0, 1],
        [1, 0]
    ]
    assert count_alive_neighbors(grid, 3, 4) == 0

# --- Edge case tests ---

def test_empty_grid(empty_grid):
    """Empty grid should always return 0 neighbors."""
    assert count_alive_neighbors(empty_grid, 0, 0) == 0

def test_single_cell_grid(single_cell_grid):
    """Single cell grid should have 0 neighbors (no adjacent cells)."""
    assert count_alive_neighbors(single_cell_grid, 0, 0) == 0

def test_full_alive_grid_center(full_alive_grid):
    """In a full grid, center has 8 alive neighbors."""
    assert count_alive_neighbors(full_alive_grid, 1, 1) == 8

def test_full_alive_grid_corner(full_alive_grid):
    """Top-left corner in a full grid should have 3 alive neighbors."""
    assert count_alive_neighbors(full_alive_grid, 0, 0) == 3

def test_full_alive_grid_edge(full_alive_grid):
    """Top edge (not corner) should have 5 alive neighbors."""
    assert count_alive_neighbors(full_alive_grid, 0, 1) == 5

def test_full_dead_grid(full_dead_grid):
    """Fully dead grid should always return 0 neighbors anywhere."""
    assert count_alive_neighbors(full_dead_grid, 1, 1) == 0
