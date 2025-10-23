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

def test_1x1_grid():
    grid = Grid(1, 1)
    assert grid.rows == 1
    assert grid.cols == 1
    assert grid.data == [[0]]

def test_empty_data_initialization():
    grid = Grid(data=[])
    assert grid.rows == 0
    assert grid.cols == 0
    assert grid.data == []

def test_get_grid_returns_same_reference():
    grid = Grid(2, 2)
    g_ref = grid.get_grid()
    g_ref[0][0] = 1
    assert grid.data[0][0] == 1
