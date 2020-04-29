class Node:
    def __init__(self,state=None,depth=None,parent=None,\
                 attacked_cells=None):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.attacked_cells = attacked_cells
