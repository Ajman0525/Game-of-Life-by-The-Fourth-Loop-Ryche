from next_generation import next_generation

def multiple_generation(grid, generations):
    """Simulate multiple generations."""
    result = grid
    for _ in range(generations):
        result = next_generation(result)
    return result

