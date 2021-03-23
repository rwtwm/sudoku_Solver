import solver.game.grid as grid
import re

class TextLoader():
    def __init__(self, grid: grid.Grid):
        self.grid = grid


    def load_cell(self, entry_str):
        mt_str = r"^\d,\d,\d$"
        print(re.match(mt_str, entry_str))
        if re.match(mt_str, entry_str) is None:
            raise Exception(entry_str)
        x, y, val = entry_str.split(",")
        cell = self.grid.get_cell(int(x), int(y))
        cell.set_val(int(val))





if __name__ == "__main__":
    grid = grid.Grid()
    loader = TextLoader(grid)
    loader.load_cell("1x,2,3")
