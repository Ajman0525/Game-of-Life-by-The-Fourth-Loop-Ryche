from count_alive_neighbors import count_alive_neighbors

def next_generation(grid):
    """
    Compute the next state of the grid according to Conway's Game of Life rules.

    Args:
        grid (list[list[int]]): 2D list where 1 = alive, 0 = dead.

    Returns:
        list[list[int]]: A new 2D list representing the next generation.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Create a deep copy to avoid mutating the original grid
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            alive_neighbors = count_alive_neighbors(grid, r, c,)
            if grid[r][c] == 1:
                # Apply rules for live cells
                if alive_neighbors < 2:       # Underpopulation
                    new_grid[r][c] = 0
                elif alive_neighbors in (2, 3):  # Survival
                    new_grid[r][c] = 1
                else:                        # Overpopulation
                    new_grid[r][c] = 0
            else:
                # Apply reproduction rule
                if alive_neighbors == 3:
                    new_grid[r][c] = 1

    return new_grid