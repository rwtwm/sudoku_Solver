import unittest
import code.game.cell as cell


class BoxTests(unittest.TestCase):

    # Cell 1,1 should be in box 1
    def test_1(self):
        box = cell.find_box(1, 1)
        self.assertEqual(box, 1)

    def test_2(self):
        box = cell.find_box(3, 3)
        self.assertEqual(box, 1)

    def test_3(self):
        box = cell.find_box(6, 3)
        self.assertEqual(box, 2)

    def test_4(self):
        box = cell.find_box(7, 5)
        self.assertEqual(box, 6)

    def test_5(self):
        box = cell.find_box(5, 7)
        self.assertEqual(box, 8)

    def test_6(self):
        box = cell.find_box(8, 9)
        self.assertEqual(box, 9)