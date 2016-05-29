from initialize import Initialize
from random_restart import RandomRestart
import numpy as np
import operator

def Update(state,col,total_conflicts):
    conflicts = np.sum(state,1)
    N = state.shape[0]
    for row in range(N):
        k = col-row
        conflicts[row] += np.sum(np.diag(state,k))

        k = N-1-col-row
        conflicts[row]+=np.sum(np.diag(np.fliplr(state),k))
        
    row = np.where(state[:,col]==1)[0][0,0]
    conflicts[row] -= 3
    conflicts_dict = dict((i,int(x[0,0])) for i,x in \
                           enumerate(conflicts))
    sorted_dict = sorted(conflicts_dict.items(),key=\
                         operator.itemgetter(1))
    state[row,col] = 0
    state[sorted_dict[0][0],col] = 1
    total_conflicts = total_conflicts+(2*sorted_dict[0][1])\
                      -(2*conflicts[row,0])
    return total_conflicts




        
