# test_read_text_file.py
from src.read_text import File


def test_read_input_file():
    file_reader = File()
    grid, generation = file_reader.read_input_file("input.txt")

    print("Grid:")
    for row in grid:
        print(row)
    print("Generation:", generation)

    assert isinstance(grid, list)
    assert all(isinstance(row, list) for row in grid)
    assert isinstance(generation, int)
