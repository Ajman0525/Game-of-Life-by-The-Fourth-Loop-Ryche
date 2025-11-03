# read_txt.py
class File:
    """
    Handles reading Conway's Game of Life input files.
    """

    def read_input_file(self, filename):
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
        with open(filename, "r") as file:
            lines = [line.rstrip("\n") for line in file.readlines()]

        population_lines = []
        generation_number = 0
        blank_found = False  # Marks the blank line that separates grid and generation count

        for line in lines:
            if line.strip() == "" and not blank_found:
                blank_found = True
                continue
            if not blank_found:
                population_lines.append(line)
            elif blank_found and line.strip().isdigit():
                generation_number = int(line.strip())
                break

        grid = [[1 if char == "*" else 0 for char in row] for row in population_lines]

        return grid, generation_number
