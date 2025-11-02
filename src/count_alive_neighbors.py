from src.world_wrapping import Grid_Wrapper

def is_in_bounds(grid, row, col):
    """
    Check if a given cell (row, col) is inside the grid boundaries.
    """
    if row < 0: # Row index is negative → above the top of the grid → out of bounds
        return False
    else:
        if row >= len(grid): # Row index beyond last row → below the grid → out of bounds
            return False
        else:
            if col < 0: # Column index is negative → left of the grid → out of bounds
                return False
            else:
                if col >= len(grid[0]): # Column index beyond last column → right of the grid → out of bounds
                    return False
                else:
                    return True # Row and column are within valid ranges → in bounds

def is_alive(grid, row, col):
    """
    Check if a given cell (row, col) is alive.
    Returns False if the cell is out of bounds.
    """
    if is_in_bounds(grid, row, col):
        if grid[row][col] == 1:
            return True
        else:
            return False
    else:
        return False

def count_alive_neighbors(grid, target_row, target_col):
    """
    Count the number of alive (1) neighboring cells around a given cell in a 2D grid.

    The grid does not wrap around edges — neighbors outside grid boundaries
    are ignored (non-wrapping behavior).
    Returns 0 if the target cell itself is out of bounds.
    """
    if is_in_bounds(grid, target_row, target_col):
        alive_neighbors = 0
        # Loop over all possible neighbors (3x3 box around the target cell)
        for current_row in range(target_row - 1, target_row + 2): # Range works from start inclusive to stop exclusive
            for current_column in range(target_col - 1, target_col + 2):
                if (current_row == target_row) and (current_column == target_col):
                    continue  # Skip the target cell itself
                else:
                    if is_alive(grid, current_row, current_column):
                        alive_neighbors += 1
        return alive_neighbors
    else:
        return 0
