import solver.game.cell


class Group:
    def __init__(self, gid):
        self.cells = []
        self.id = gid

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

    # Note this takes a list. Use get solved to guarantee a list,
    # or wrap a single value in a list before submission
    def clear_possibles(self, poss_list):
        for val in poss_list:
            self.remove_possible(val)


class Row(Group):
    pass


class Column(Group):
    pass


class Box(Group):
    pass