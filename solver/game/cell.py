import math


def find_box(x, y):
    sub_y = y - 1
    y_add = sub_y - (sub_y % 3)
    return math.ceil(x/3) + y_add


class Cell:
    def __init__(self, x, y):
        '''
        Class to represent the cell of a sudoku grid.
        :param x: The column of the cell (left to right)
        :param y: The row of the cell (top to bottom)
        '''
        self.row = x
        self.col = y
        self.box = find_box(x, y)
        self.poss_vals = [i for i in range(1,10)]
        self.conf_val = 0   # Not sure how to represent no val. 0 will do for now.

    def set_val(self, val):
        '''
        Sets the value of the cell, and empties the poss_vals list
        :param val: The confirmed value of the cell
        '''
        self.poss_vals = []
        self.conf_val = val

    def remove_poss_val(self, val):
        '''
        Called when a conf_val is added to a row, col or box to
        remove the poss_val from the other entries in that group
        :param val: The value to remove
        '''
        if val in self.poss_vals:
            self.poss_vals.remove(val)

    def __str__(self):
        '''
        Prints the current cell status.
        '''
        part1 = "cell coordinate: ({0},{1}). ".format(self.col, self.row)
        if self.conf_val != 0:
            part2 = "val = {}.".format(self.conf_val)
        else:
            part2 = "possible vals: " + str(self.poss_vals)
        return part1 + part2



