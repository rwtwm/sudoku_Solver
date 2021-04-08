import unittest

from solver.game import grid
from solver.game import text_loader as load


# Tests the to string, and check value resolution features of the cell object.
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        path = r'D:\Documents\01 Python\0110 SudokuSolver\sudoku_Solver\Text\SampleGridCorr.txt'
        cls._grid = grid.Grid()
        cls._loader = load.TextLoader(cls._grid)
        cls._loader.load_grid(path)

    def test_get_value(self):
        cell = self._grid.get_cell(1, 0)
        self.assertEqual(cell.conf_val, 4)

    # If a value has been successfully set the possible values should be empty
    def test_set_value(self):
        cell = self._grid.get_cell(3,0)
        cell.set_val(8)
        self.assertEqual(cell.poss_vals, [])

    # No assert on this one, just printing some strings to the console
    def test_cell_prints(self):
        cell1 = self._grid.get_cell(2, 4)
        cell2 = self._grid.get_cell(4, 3)
        print(cell1)
        print(cell2)
        self.assertTrue(True)

    def test_remove_vals(self):
        pass


if __name__ == '__main__':
    unittest.main()
