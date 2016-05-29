import copy
from node import Node

def NewNode(node,action):
    orientation = node.orientation
    posx,posy = node.posx,node.posy
    path_cost = node.path_cost-1
    state = copy.deepcopy(node.state)
    if action == "RIGHT":
        orientation = (orientation+90)%360
    elif action == "LEFT":
        orientation = (orientation-90)%360
    elif action == "SUCK":
        path_cost += 100
        state[posx,posy] = 0
    elif action == "FORWARD":
        if orientation == 0:
            posx -= 1
        elif orientation == 90:
            posy += 1
        elif orientation == 180:
            posx += 1
        else:
            posy -= 1
    
    return Node(state=state,posx=posx,posy=posy,orientation=\
           orientation,path_cost=path_cost,depth=node.depth\
           +1,parent=node,action=action)
