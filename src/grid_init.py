class Grid:
    def __init__(self, rows=10, cols=10, data=None):
        if data is not None:
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0]) if self.rows > 0 else 0
        else:
            self.rows = rows
            self.cols = cols
            self.data = [[0] * cols for _ in range(rows)]
    
    def get_grid(self):
        return self.data
