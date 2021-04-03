import unittest
import solver.game.grid as grid
import solver.game.text_loader as loader

class MyTestCase(unittest.TestCase):
    def test_drawing(self):
        test_grid = grid.Grid()
        ldr = loader.TextLoader(test_grid)
        ldr.load_cell("0,1,3")
        ldr.load_cell("2,4,8")
        ldr.load_cell("0,3,9")
        ldr.load_cell("8,5,2")
        test_grid.print_grid()


if __name__ == '__main__':
    unittest.main()
