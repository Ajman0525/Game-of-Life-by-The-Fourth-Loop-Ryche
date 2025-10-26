from display import display_grid
from grid_init import Grid

def get_grid_size():
    while True:
        try:
            rows = int(input("Enter number of rows (5-20): "))
            cols = int(input("Enter number of columns (5-20): "))
            if 5 <= rows <= 20 and 5 <= cols <= 20:
                return rows, cols
            print("Please enter values between 5 and 20")
        except ValueError:
            print("Please enter valid numbers")
            
# Create initial grid with user-defined live cells
# The input_func parameter allows for dependency injection of the input function for easier testing
def create_initial_grid(rows, cols, input_func=input):
    # Initialize grid using Grid class
    grid_obj = Grid(rows, cols)
    grid = grid_obj.get_grid()
    
    print("\nEnter coordinates for live cells (row,col), e.g., '2,3'. Enter 'done' when finished:")
    print("Note: Coordinates start from 0,0 (top-left corner)")
    
    while True:
        coord = input_func("Enter coordinates (or 'done'): ").strip().lower()
        if coord == 'done':
            break
        
        try:
            row, col = map(int, coord.split(','))
            if 0 <= row < rows and 0 <= col < cols:
                grid[row][col] = 1
                print("\nCurrent grid:")
                print(display_grid(grid))
            else:
                print(f"Coordinates must be between 0,0 and {rows-1},{cols-1}")
        except ValueError:
            print("Invalid format. Use 'row,col' (e.g., '2,3')")
    
    return grid

def main():
    print("Welcome to Conway's Game of Life!")
    
    # Get grid size from user
    rows, cols = get_grid_size()
    
    # Get initial grid configuration
    initial_grid = create_initial_grid(rows, cols)
    current_grid = initial_grid
    

if __name__ == "__main__":
    main()
