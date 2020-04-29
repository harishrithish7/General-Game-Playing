import numpy as np

def PossibleAction(node):
    actions = ["LEFT","RIGHT"]
    posx,posy,state = node.posx,node.posy,node.state
    orientation = node.orientation
    if orientation == 0 and posx > 0 and \
       state[posx-1,posy] in [0,1]:
        actions.append("FORWARD")
    elif orientation == 90 and posy < state.shape[1]-1 and \
         state[posx,posy+1] in [0,1]:
        actions.append("FORWARD")
    elif orientation == 180 and posx < state.shape[0]-1 and\
         state[posx+1,posy] in [0,1]:
        actions.append("FORWARD")
    elif orientation == 270 and posy > 0 and \
         state[posx,posy-1] in [0,1]:
        actions.append("FORWARD")
    if state[posx,posy] == 1:
        actions.append("SUCK")
    if not 1 in state:
        actions.append("TURN OFF")

    return actions
        
        
