import numpy as np
import random
def PrepareEnvironment():
    global state
    random.seed()
    M = random.randint(8,15)
    N = random.randint(8,15)
    state = np.zeros((M,N))
    
    for ridx,row in enumerate(state):
        for cidx,cell in enumerate(row):
            if random.randint(1,100) < 6:
                state[ridx,cidx] = 1
    return  state

print PrepareEnvironment()
