from src.world_wrapping import Grid_Wrapper
def test_world_wrapping_from_start_to_end():
    DIMENSION_SIZE = 10
    connect = Grid_Wrapper(size=DIMENSION_SIZE)

    current_coordinate = 0
    change_in_coordinate = -1

    assert connect.world_wrap(current_coordinate, change_in_coordinate) == 9