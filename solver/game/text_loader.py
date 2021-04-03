import solver.game.grid as grid
import re

class TextLoader():
    def __init__(self, grid: grid.Grid):
        self.grid = grid

    # Loads a single cell based on an input string of format #,#,#
    def load_cell(self, entry_str):
        mt_str = r"^\d,\d,\d$"
        print(re.match(mt_str, entry_str))
        if re.match(mt_str, entry_str) is None:
            raise Exception(entry_str)
        x, y, val = entry_str.split(",")
        cell = self.grid.get_cell(int(x), int(y))
        cell.set_val(int(val))

    # For loading the starting grid layout based on a text file location.
    def load_grid(self, text_file):
        inbound = open(text_file, 'r')
        for line in inbound.readlines():
            self.load_cell(line)
        inbound.close()


if __name__ == "__main__":
    path = r'D:\Documents\01 Python\0110 SudokuSolver\sudoku_Solver\Text\SampleGridCorr.txt'
    grid = grid.Grid()
    loader = TextLoader(grid)
    loader.load_grid(path)
    grid.print_grid()
