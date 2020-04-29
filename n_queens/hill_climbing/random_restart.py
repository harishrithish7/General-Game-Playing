import random
import numpy as np

def RandomRestart(state,col,total_conflicts):
    N = state.shape[0]
    row = np.where(state[:,col]==1)[0][0,0]
    conflicts = np.sum(state[row,:])
    k = col-row
    conflicts += np.sum(np.diag(state,k))
    k = N-1-col-row
    conflicts += np.sum(np.diag(np.fliplr(state),k))
    conflicts -= 3
    total_conflicts = total_conflicts-(2*conflicts)
    state[row,col] = 0
    
    state[random.randint(0,N-1),col] = 1
    row = np.where(state[:,col]==1)[0][0,0]
    conflicts = np.sum(state[row,:])
    k = col-row
    conflicts += np.sum(np.diag(state,k))
    k = N-1-col-row
    conflicts += np.sum(np.diag(np.fliplr(state),k))
    conflicts -= 3
    total_conflicts = total_conflicts+(2*conflicts)
    return total_conflicts




