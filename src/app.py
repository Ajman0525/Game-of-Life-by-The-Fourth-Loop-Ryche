from display import display_grid

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
            
def main():
    print("Welcome to Conway's Game of Life!")
    
    # Get grid size from user
    rows, cols = get_grid_size()
    

if __name__ == "__main__":
    main()
