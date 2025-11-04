
# Tests for Get_grid_size

from src.app import get_grid_size

def test_get_grid_size_valid(monkeypatch):
    inputs = iter(["5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_grid_size()
    assert result == (5, 5)

    inputs = iter(["20", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_grid_size()
    assert result == (20, 20)

    inputs = iter(["10", "15"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_grid_size()
    assert result == (10, 15)

def test_get_grid_size_invalid(monkeypatch, capsys):
    inputs = iter(["4", "3", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter values between 5 and 20" in captured.out

    inputs = iter(["21", "22", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter values between 5 and 20" in captured.out

    inputs = iter(["abc", "def", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter valid numbers" in captured.out

    inputs = iter(["5", "abc", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter valid numbers" in captured.out



# Tests for create_initial_grid function

from src.app import create_initial_grid

def _make_empty(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def test_done_immediately(capsys):
    inputs = iter(["done"])
    def fake_input(prompt): return next(inputs)
    grid = create_initial_grid(3, 4, input_func=fake_input)
    assert grid == _make_empty(3, 4)
    out = capsys.readouterr().out
    assert "Enter coordinates for live cells" in out

def test_single_valid_coordinate(capsys):
    inputs = iter(["1,2", "done"])
    def fake_input(prompt): return next(inputs)
    grid = create_initial_grid(3, 4, input_func=fake_input)
    expected = _make_empty(3, 4)
    expected[1][2] = 1 
    assert grid == expected
    out = capsys.readouterr().out
    assert "Current grid:" in out

def test_multiple_valid_coordinates(capsys):
    inputs = iter(["0,0", "2,3", "1,1", "done"])
    def fake_input(prompt): return next(inputs)
    grid = create_initial_grid(3, 4, input_func=fake_input)
    expected = _make_empty(3, 4)
    expected[0][0] = 1  
    expected[2][3] = 1  
    expected[1][1] = 1  
    assert grid == expected

def test_out_of_bounds_then_valid(capsys):
    inputs = iter(["5,5", "1,1", "done"])
    def fake_input(prompt): return next(inputs)
    grid = create_initial_grid(3, 3, input_func=fake_input)
    expected = _make_empty(3, 3)
    expected[1][1] = 1  
    assert grid == expected
    out = capsys.readouterr().out
    assert "Coordinates must be between 0,0 and 2,2" in out

def test_invalid_format_then_valid(capsys):
    inputs = iter(["abc", "1,0", "done"])
    def fake_input(prompt): return next(inputs)
    grid = create_initial_grid(2, 2, input_func=fake_input)
    expected = _make_empty(2, 2)
    expected[1][0] = 1  
    assert grid == expected
    out = capsys.readouterr().out
    assert "Invalid format. Use 'row,col'" in out

def test_whitespace_and_case_handling(capsys):
    inputs = iter([" 2 , 1 ", " DONE "])
    def fake_input(prompt): return next(inputs)
    grid = create_initial_grid(4, 4, input_func=fake_input)
    expected = _make_empty(4, 4)
    expected[2][1] = 1  # Whitespace and case should be handled
    assert grid == expected
