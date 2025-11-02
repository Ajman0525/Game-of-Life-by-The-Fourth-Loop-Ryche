from src.world_wrapping import Grid_Wrapper

NEIGHBOR_OFFSETS = [
    (-1, -1), (0, -1), (1, -1), 
    (-1, 0),           (1, 0),   
    (-1, 1),  (0, 1),  (1, 1)     
]

def count_alive_neighbors(grid, target_row, target_col):
    rows = len(grid)
    columns = len(grid[0]) if rows > 0 else 0

    wrapper = Grid_Wrapper(width=columns, height=rows)
    
    alive_neighbors = 0

    for offset_column, offset_row in NEIGHBOR_OFFSETS:
        wrapped_row = wrapper.world_wrap(target_row, offset_row, is_x_axis=False) 
        wrapped_column = wrapper.world_wrap(target_col, offset_column, is_x_axis=True)
        
        if grid[wrapped_row][wrapped_column] == 1:
            alive_neighbors += 1

    return alive_neighbors
