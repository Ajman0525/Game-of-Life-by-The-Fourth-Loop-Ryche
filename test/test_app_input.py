from src.app import get_grid_size

def test_get_grid_size_valid(monkeypatch):
    # Simulate user entering 5 and 5
    inputs = iter(["5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_grid_size()
    assert result == (5, 5)

    # Simulate user entering 20 and 20
    inputs = iter(["20", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_grid_size()
    assert result == (20, 20)

    # Simulate user entering 10 and 15
    inputs = iter(["10", "15"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_grid_size()
    assert result == (10, 15)

def test_get_grid_size_invalid(monkeypatch, capsys):
    # Simulate user entering 4 and 3 (invalid), then 5 and 5 (valid)
    inputs = iter(["4", "3", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter values between 5 and 20" in captured.out

    # Simulate user entering 21 and 22(invalid), then 5 and 5 (valid)
    inputs = iter(["21", "22", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter values between 5 and 20" in captured.out

    # Simulate user entering 'abc' and 'def' (invalid), then 5 and 5 (valid)
    inputs = iter(["abc", "def", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter valid numbers" in captured.out

    # Simulate user entering 5, then 'abc' (invalid), then 5 (valid)
    inputs = iter(["5", "abc", "5", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    get_grid_size()
    captured = capsys.readouterr()
    assert "Please enter valid numbers" in captured.out
