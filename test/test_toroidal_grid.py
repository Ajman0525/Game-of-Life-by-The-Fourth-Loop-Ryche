from src.world_wrapping import Grid_Wrapper
def test_world_wrapping():
    connect = Grid_Wrapper()

    assert connect.world() is True