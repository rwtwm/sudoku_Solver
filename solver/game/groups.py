import solver.game.cell


class Group:
    def __init__(self):
        self.cells = []
        self.id = 0

    def remove_possible(self, val):
        for cell in self.cells:
            cell.remove_poss_val(val)

    # Returns a list of all confirmed values in the group
    def get_solved(self):
        in_group = []
        for cell in self.cells:
            if cell.conf_val != 0:
                in_group.append(cell.conf_val)
        return in_group


class Row(Group):
    pass


class Column(Group):
    pass


class Box(Group):
    pass