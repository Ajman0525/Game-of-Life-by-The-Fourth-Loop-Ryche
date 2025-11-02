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

def count_alive_neighbors(grid, row, col):
    """Count the number of alive (1) neighbors around a cell."""
    if not grid or row < 0 or col < 0:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Out of bounds safety check
    if row >= rows or col >= cols:
        return 0

    count = 0
    # Check all 8 directions
    for i in range(-1, 2):     # -1, 0, +1
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # skip the cell itself
            r, c = row + i, col + j
            if 0 <= r < rows and 0 <= c < cols:
                count += grid[r][c]
    return count


