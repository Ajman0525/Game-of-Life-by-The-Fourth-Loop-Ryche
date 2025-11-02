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
    