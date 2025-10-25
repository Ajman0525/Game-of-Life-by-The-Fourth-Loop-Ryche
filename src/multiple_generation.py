from src.generation import next_generation

def multiple_generation(initial_grid, total_generations):
    """
    Evolve the Game of Life grid for a number of generations
    and return the final grid state.
    """

    # Create a full copy of the initial grid (to avoid changing the original)
    grid_copy = []
    for row in initial_grid:
        new_row = []
        for cell in row:
            new_row.append(cell)
        grid_copy.append(new_row)

    # Keep track of the grid as it changes
    current_grid = grid_copy

    # Step through each generation one by one
    for generation_number in range(total_generations):
        next_grid = next_generation(current_grid)
        current_grid = next_grid

    return current_grid
