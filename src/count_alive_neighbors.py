from src.world_wrapping import Grid_Wrapper

NEIGHBOR_OFFSETS = [
    (-1, -1), (0, -1), (1, -1), 
    (-1, 0),           (1, 0),   
    (-1, 1),  (0, 1),  (1, 1)     
]

def count_alive_neighbors(grid, target_row, target_col):
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
