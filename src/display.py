from grid_init import Grid


def display_grid(grid):
    """Return a visual representation of the grid."""
    if not grid:
        return ""
    return "\n".join("".join("⬜" if cell == 1 else "⬛" for cell in row) + " " for row in grid) + "\n"


