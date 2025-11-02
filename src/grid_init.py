from read_text import File

# Create file reader instance
file_reader = File()

# Example: read the input file
grid, generation = file_reader.read_input_file("input.txt")

# Initialize grid object
from grid_init import Grid
grid_obj = Grid(data=grid)

