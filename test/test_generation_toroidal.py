from src.next_generation import next_generation

def test_toroidal_reproduction_in_center():
    initial_grid = [
        [1, 0, 1],
        [0, 0, 0],
        [0, 0, 1]
    ]
    
    
    expected_grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]  
    assert next_generation(initial_grid) == expected_grid
