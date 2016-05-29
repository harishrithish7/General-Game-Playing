import numpy as np
import copy
from node import Node

def ExpandNode(fringe,node):
    domain = [7,6,5,4,3,2,1,0]
    row = node.depth
    state = node.state
    for col in domain:
        if np.sum(state[:,col])>=1 or np.sum(state[row,:])>=1:
            continue
        k = col-row
        if np.sum(np.diag(state,k)) >= 1:
            continue
        k = 7-col-row
        if np.sum(np.diag(np.fliplr(state),k)) >= 1:
            continue
        nstate = copy.deepcopy(state)
        nstate[row,col] = 1
        new_node = Node(parent=node,depth=node.depth\
                               +1,state=nstate)
        fringe.insert(0,new_node)
        

