from src.display import display_grid
from src.next_generation import next_generation


def test_dead_cells_display_default_grid():
    grid = [[0] * 10 for _ in range(10)]
    expected_output = "".join((["⬛" * 10 + " \n"] * 10))
    assert display_grid(grid) == expected_output


def test_alive_cells_display_default_grid():
    grid = [[1] * 10 for _ in range(10)]
    expected_output = "".join((["⬜" * 10 + " \n"] * 10))
    assert display_grid(grid) == expected_output


def test_mixed_cells_display():
    grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    expected_output = "⬛⬜⬛ \n⬜⬛⬜ \n⬛⬜⬛ \n"
    assert display_grid(grid) == expected_output


def test_empty_grid_display():
    grid = []
    expected_output = ""
    assert display_grid(grid) == expected_output


def test_two_dead_neighbours():
    initial_grid = [[1, 1, 1], [1, 1, 1], [1, 0, 0]]
    expected_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  
    next_generation(initial_grid) == expected_grid
    assert display_grid(next_generation(initial_grid)) == display_grid(expected_grid)


def test_single_alive_cell():
    initial_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    next_generation(initial_grid) == expected_grid
    assert display_grid(next_generation(initial_grid)) == display_grid(expected_grid)


def test_non_square_grid_display():
    grid = [[0, 1, 0, 1], [1, 0, 1, 0]]
    expected_output = "⬛⬜⬛⬜ \n⬜⬛⬜⬛ \n"
    assert display_grid(grid) == expected_output


def test_large_grid_display():
    grid = [[(i + j) % 2 for j in range(20)] for i in range(10)]
    expected_output = ""
    for i in range(10):
        row_str = ""
        for j in range(20):
            row_str += "⬜" if (i + j) % 2 == 1 else "⬛"
        expected_output += row_str + " \n"
    assert display_grid(grid) == expected_output
