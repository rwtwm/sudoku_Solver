import code.game.cell


class group:
    def __init__(self):
        self.cells = []
        self.id = 0

    def remove_possible(self, val):
        for cell in self.cells:
            cell.remove_poss_val(val)


class Row(group):
    pass


class Column(group):
    pass


class Box(group):
    pass