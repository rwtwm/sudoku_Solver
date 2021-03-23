import unittest

from solver.game.grid import Grid
from solver.game.text_loader import TextLoader


class MyTestCase(unittest.TestCase):
    def test_load_cell(self):
        grid = Grid()
        loader = TextLoader(grid)
        loader.load_cell("0,2,3")
        cell_value = grid.get_cell(0, 2).conf_val
        self.assertEqual(cell_value, 3)

    def test_exception(self):
        grid = Grid()
        loader = TextLoader(grid)
        with self.assertRaises(Exception):
            loader.load_cell("0x2,3")




