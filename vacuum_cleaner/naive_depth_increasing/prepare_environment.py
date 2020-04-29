import numpy as np
import random

def PrepareEnvironment():
    N=5
    state = np.mat( np.zeros((N,N)) )
    state[0,1] = 1
    state[2,4] = 1
    state[1,3] = 1
    state[3,0] = 1
    return state,0,0,0
    """random.seed()
    M = random.randint(8,15)
    N = random.randint(8,15)
    state = np.zeros((M,N))
    
    for ridx,row in enumerate(state):
        for cidx,cell in enumerate(row):
            if random.randint(1,100) < 6:
                state[ridx,cidx] = 1
    return  state"""
