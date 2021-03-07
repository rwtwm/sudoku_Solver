import unittest
import solver.game.grid as grid

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_grid = grid.Grid()
        test_grid.populate_empty_cells()
        test_grid.print_grid()



if __name__ == '__main__':
    unittest.main()
