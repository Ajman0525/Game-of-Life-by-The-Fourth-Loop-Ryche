def read_input_file(filename):
    """
    Reads a Conway's Game of Life input file and returns:
      - a 2D list (grid) representing the initial population
      - the generation number to simulate

    Expected file format example:
        ..........
        ..*.......
        ...*......
        .***......
        ..........
        ..........
        
        3

    Where:
        - '.' means a dead cell (0)
        - '*' means a live cell (1)
        - The number at the end represents the generation count
    """
    # Open the input file and read all lines, removing newline characters
    with open(filename, "r") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Initialize containers for grid lines and generation number
    population_lines = []
    generation_number = 0
    blank_found = False  # Marks the blank line that separates grid and generation count

    # Process each line from the input
    for line in lines:
        if line.strip() == "" and not blank_found:
            # The first blank line separates grid and generation count
            blank_found = True
            continue
        if not blank_found:
            # Collect grid rows before the blank line
            population_lines.append(line)
        elif blank_found and line.strip().isdigit():
            # Once blank line is found, the next numeric line is generation count
            generation_number = int(line.strip())
            break

    # Convert population lines into a 2D grid (list of lists)
    # '*' becomes 1 (alive), '.' becomes 0 (dead)
    grid = [[1 if char == "*" else 0 for char in row] for row in population_lines]

    return grid, generation_number
