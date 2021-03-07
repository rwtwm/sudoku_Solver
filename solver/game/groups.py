import solver.game.cell


class Group:
    def __init__(self):
        self.cells = []
        self.id = 0

    def remove_possible(self, val):
        for cell in self.cells:
            cell.remove_poss_val(val)


class Row(Group):
    pass


class Column(Group):
    pass


class Box(Group):
    pass