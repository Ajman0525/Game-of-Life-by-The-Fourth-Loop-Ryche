class Grid_Wrapper:
    def __init__(self,width, height):
        self.grid_width = width
        self.grid_height = height

    def calculate_wrapped_index(self, current_coord,change_in_coord, max_size):
        new_index_coordinate = current_coord + change_in_coord
        wrapped_coordinate = (new_index_coordinate % max_size + max_size) % max_size

        return wrapped_coordinate

    def world_wrap(self, current_coordinate, change_in_coordinate, is_x_axis):
        max_size = self.grid_width if is_x_axis else self.grid_height
        
        return self.calculate_wrapped_index(
            current_coordinate, 
            change_in_coordinate, 
            max_size
        )
    def find_all_neighbors(self, current_x, current_y):
        neighbor_coordinates = []
        NEIGHBOR_OFFSETS = [
            (-1, -1),(0, -1),(1, -1), 
            (-1, 0),         (1, 0),   
            (-1, 1), (0, 1), (1, 1)
        ]
        for dx, dy in NEIGHBOR_OFFSETS:
            # X uses is_x_axis=True
            wrapped_x = self.world_wrap(current_x, dx, is_x_axis=True)
            
            # Y uses is_x_axis=False
            wrapped_y = self.world_wrap(current_y, dy, is_x_axis=False) 
            
            neighbor_coordinates.append((wrapped_x, wrapped_y))
            
        return neighbor_coordinates