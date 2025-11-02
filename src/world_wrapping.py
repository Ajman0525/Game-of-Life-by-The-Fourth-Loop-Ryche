class Grid_Wrapper:
    def __init__(self,width, height):
        self.grid_width = width
        self.grid_height = height

    def world_wrap(self, current_coordinate,change_in_coordinate, total_cells):
        new_index_coordinate = current_coordinate + change_in_coordinate
        wrapped_coordinate = (new_index_coordinate % total_cells + total_cells) % total_cells

        return wrapped_coordinate

