import numpy as np
import copy
from node import Node

def ExpandNode(fringe,node):
    domain = [7,6,5,4,3,2,1,0]
    row = node.depth
    state = node.state
    for col in domain:
        if node.attacked_cells[row,col]:
            continue
        attacked_cells = copy.deepcopy(node.attacked_cells)
        attacked_cells[:,col] = 1
        attacked_cells[row,:] = 1
        k = row-col
        rows, cols = np.diag_indices_from(attacked_cells)
        if k < 0:
            rows,cols = rows[:k],cols[-k:]
        elif k > 0:
            rows,cols = rows[k:],cols[:-k]
        attacked_cells[rows,cols] = 1

        attacked_cells = np.fliplr(attacked_cells)
        ncol = 7-col
        k = row-ncol
        rows, cols = np.diag_indices_from(attacked_cells)
        if k < 0:
            rows,cols = rows[:k],cols[-k:]
        elif k > 0:
            rows,cols = rows[k:],cols[:-k]
        attacked_cells[rows,cols] = 1
        attacked_cells = np.fliplr(attacked_cells)

        valid = True
        for i in range(node.depth+1,8):
            if np.sum(attacked_cells[i,:]) == 8:
                valid = False
                break
        if not valid:
            continue
        
        nstate = copy.deepcopy(state)
        nstate[row,col] = 1
        new_node = Node(parent=node,depth=node.depth\
             +1,state=nstate,attacked_cells=attacked_cells)
        fringe.insert(0,new_node)
        

