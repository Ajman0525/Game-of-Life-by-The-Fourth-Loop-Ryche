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


