from grid_init import Grid


def display_grid(grid):
    current_grid = Grid(data=grid).get_grid()
    dead_cell, alive_cell = '⬛', '⬜'
    display_str = ""
    for row in current_grid:
        for cell in row:
            if cell == 1:
                display_str += alive_cell
            else:
                display_str += dead_cell
        display_str += " \n"
    return display_str

