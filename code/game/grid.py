from code.game.cell import Cell
from code.game.groups import Row, Column, Box

class Grid():
    '''
    Represents the grid object. As only one is likely to be created
    it could be argued that a class isn't needed, but it helps in storing the state.
    '''
    def __init__(self):
        self.cells = []
        self.rows = []
        self.columns = []
        self.boxes = []

    def populate_empty_cells(self):
        for x in range(1, 10):
            for y in range(1, 10):
                self.cells.append(Cell(x, y))

    def generate_groups(self):
        for cell in self.cells:
            self.rows[cell.row].cells.append(cell)
            self.columns[cell.col].cells.append(cell)
            self.boxes[cell.box].cells.append(cell)

    def create_rows(self):
        for y in range(1, 10):
            self.rows.append(Row())

    def create_columns(self):
        for x in range(1, 10):
            self.columns.append(Column())

    def create_boxes(self):
        for y in range(1, 10):
            self.columns.append(Column())

    def print_grid(self):
        pass