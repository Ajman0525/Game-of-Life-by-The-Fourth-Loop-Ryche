import pytest
from src.count_alive_neighbors import count_alive_neighbors

def test_center_cell_in_3x3_grid_with_two_neighbors():
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 2

def test_corner_cell_in_2x2_grid_with_two_neighbors():
    grid = [
        [0, 1],
        [1, 0]
    ]
    assert count_alive_neighbors(grid, 0, 0) == 4

def test_edge_cell_in_cross_pattern_has_four_neighbors():
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert count_alive_neighbors(grid, 1, 0) == 3


def test_center_cell_in_cross_pattern_has_four_neighbors():
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 4

# --- Edge case tests ---

def test_empty_grid_returns_zero_neighbors():
    grid = []
    assert count_alive_neighbors(grid, 0, 0) == 0


def test_single_cell_grid_has_zero_neighbors():
    grid = []
    assert count_alive_neighbors(grid, 0, 0) == 0


def test_full_alive_grid_center_has_eight_neighbors():
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
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert count_alive_neighbors(grid, 1, 1) == 0