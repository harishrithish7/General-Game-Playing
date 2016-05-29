import random
import numpy as np

def Initialize(N):
    state = np.mat(np.zeros((N,N)),dtype='int32')
    random.seed()
    for col in range(N):
        row = random.randint(0,N-1)
        state[row,col] = 1
    return state


