from src.world_wrapping import grid
def test_world_wrapping():
    connect = grid()

    assert connect.world() is True