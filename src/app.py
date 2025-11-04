from display import display_grid
from grid_init import Grid
from next_generation import next_generation
from multiple_generation import multiple_generation
import time

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
            
def create_initial_grid(rows, cols, input_func=input):
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


def display_menu():
    print("\nOptions:")
    print("1. Next generation")
    print("2. Run multiple generations")
    print("3. Reset grid")
    print("4. Exit")
    return input("Choose an option (1-4): ")

def main():
    print("Welcome to Conway's Game of Life!")
    
    rows, cols = get_grid_size()
    
    initial_grid = create_initial_grid(rows, cols)
    current_grid = initial_grid
    
    while True:
        print("\nCurrent grid:")
        print(display_grid(current_grid))
        
        choice = display_menu()
        
        if choice == '1':
            current_grid = next_generation(current_grid)
            
        elif choice == '2':
            try:
                gens = int(input("How many generations? "))
                if gens > 0:
                    for gen in range(gens):
                        current_grid = multiple_generation(current_grid, 1)
                        print("\033[H\033[J")  # Clear screen
                        print(f"Generation {gen + 1}:")
                        print(display_grid(current_grid))
                        time.sleep(0.5)
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '3':
            current_grid = create_initial_grid(rows, cols)
        
        elif choice == '4':
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid option. Please choose 1-4")

if __name__ == "__main__":
    main()
