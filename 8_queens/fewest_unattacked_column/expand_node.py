import numpy as np
import copy
from node import Node
import operator

def ExpandNode(fringe,node):
    col_sum = np.sum(node.attacked_cells,0)
    dict_sum = {}
    for i in range(8):
        if col_sum[0,i] == 8:
            continue
        dict_sum[i] = col_sum[0,i]
    sorted_sum = sorted(dict_sum.items(),key=operator.\
                        itemgetter(1),reverse=True)
    for i in range(len(sorted_sum)):
        col = sorted_sum[i][0]
        for row in range(8):
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
            
            nstate = copy.deepcopy(node.state)
            nstate[row,col] = 1
            new_node = Node(parent=node,depth=node.depth\
                 +1,state=nstate,attacked_cells=attacked_cells)
            fringe.insert(0,new_node)
        

