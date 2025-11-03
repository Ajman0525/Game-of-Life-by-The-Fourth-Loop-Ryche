from count_alive_neighbors import count_alive_neighbors

def next_generation(grid):
    """Compute next generation without mutating the original grid."""
    if not grid:
        return []

    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            neighbors = count_alive_neighbors(grid, r, c)
            if grid[r][c] == 1:
                # Live cell survives if it has 2 or 3 neighbors
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                # Dead cell becomes alive if it has exactly 3 neighbors
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid
