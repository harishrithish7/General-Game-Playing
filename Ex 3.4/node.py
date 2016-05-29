class Node:
    def __init__(self,state=None,parent=None,depth=None,\
                 path_cost=None,action=None):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.path_cost = path_cost
        self.action = action
