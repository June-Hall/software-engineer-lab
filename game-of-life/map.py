import numpy as np

class Map:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = np.zeros((self.height // self.cell_size, self.width // self.cell_size))

    def set_cell_state(self, row, col, state):
        self.cells[row, col] = state

    def get_cell_state(self, row, col):
        return self.cells[row, col]

    def update_cells(self):
        updated_cells = np.zeros_like(self.cells)

        for row, col in np.ndindex(self.cells.shape):
            alive = np.sum(self.cells[row - 1: row + 2, col - 1: col + 2]) - self.cells[row, col]

            if self.cells[row, col] == 1:
                if alive < 2 or alive > 3:
                    updated_cells[row, col] = 0
                else:
                    updated_cells[row, col] = 1
            elif alive == 3:
                updated_cells[row, col] = 1

        self.cells = updated_cells
