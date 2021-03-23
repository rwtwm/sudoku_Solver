from solver.game.cell import Cell
from solver.game.groups import Row, Column, Box

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
        self.populate_empty_cells()
        self.generate_groups()


    def populate_empty_cells(self):
        for x in range(0, 9):
            for y in range(0, 9):
                self.cells.append(Cell(x, y))

    def generate_groups(self):
        for cell in self.cells:
            self.create_rows()
            self.create_columns()
            self.create_boxes()
            self.rows[cell.row].cells.append(cell)
            self.columns[cell.col].cells.append(cell)
            self.boxes[cell.box].cells.append(cell)

    def create_rows(self):
        for y in range(0, 9):
            self.rows.append(Row())

    def create_columns(self):
        for x in range(0, 9):
            self.columns.append(Column())

    def create_boxes(self):
        for y in range(0, 9):
            self.boxes.append(Box())

    #Returns a cell, by its xy coordinates
    def get_cell(self, x, y) -> Cell:
        return self.columns[x].cells[y]

    def print_grid(self):
        for y in range(0, 9):
            row_string = ""
            for x in range(0, 9):
                row_string = row_string + str(self.rows[y].cells[x].conf_val) + " "
            print(row_string)