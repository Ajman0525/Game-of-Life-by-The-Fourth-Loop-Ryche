class Grid_Wrapper:
    def __init__(self,size):
        self.dimension_size = size

    def world_wrap(self, current_coordinate,change_in_coordinate):
        new_index_coordinate = current_coordinate + change_in_coordinate
        size = self.dimension_size
        wrapped_coordinate = (new_index_coordinate % size + size) % size

        return wrapped_coordinate

