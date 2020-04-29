class Node:
    def __init__(self,state=None,posx=None,posy=None,depth=\
                 None,path_cost=None,parent=None,orientation\
                 =None,action=None):
        self.state = state
        self.posx = posx
        self.posy = posy
        self.depth = depth
        self.path_cost = path_cost
        self.parent = parent
        self.orientation = orientation
        self.action = action
