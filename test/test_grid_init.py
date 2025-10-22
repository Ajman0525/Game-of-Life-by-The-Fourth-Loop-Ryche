from src.grid_init import Grid

def test_grid_initialization():

    # Test default initialization
    grid_default = Grid()
    assert grid_default.rows == 10  # Assuming default rows is 10
    assert grid_default.cols == 10  # Assuming default cols is 10
    assert grid_default.data == [[0]*10 for _ in range(10)] 

def test_get_grid():
    grid = Grid(3, 4)
    result = grid.get_grid()
    assert result == [[0]*4 for _ in range(3)]  
