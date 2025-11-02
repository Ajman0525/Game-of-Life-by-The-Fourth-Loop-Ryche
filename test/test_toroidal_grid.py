from src.world_wrapping import Grid_Wrapper
def test_world_wrapping_from_start_to_end():
    DIMENSION_SIZE = 10
    connect = Grid_Wrapper(width=DIMENSION_SIZE, height=DIMENSION_SIZE)

    current_coordinate = 0
    change_in_coordinate = -1

    assert connect.world_wrap(current_coordinate, change_in_coordinate, is_x_axis=True) == 9

def test_find_all_neighbors_at_top_left_corner():
    NEIGHBOR_OFFSETS = [
        (-1, -1),(0, -1),(1, -1), 
        (-1, 0),         (1, 0),   
        (-1, 1), (0, 1), (1, 1)
    ]
    WIDTH, HEIGHT = 3
    connect = Grid_Wrapper(width=WIDTH, height=HEIGHT)

    current_x_coordinate, current_y_coordinate = 0,0
    neighbors_found = connect.find_all_neighbors(current_x_coordinate, current_y_coordinate)

    expected_set = set([
        (2, 2), (2, 0), (2, 1), 
        (0, 2),         (0, 1), 
        (1, 2), (1, 0), (1, 1)  
    ])
    
    assert set(neighbors_found) == expected_set