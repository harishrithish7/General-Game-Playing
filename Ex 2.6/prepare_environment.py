import numpy as np
import random

def PrepareEnvironment():
    state = np.zeros((2,2))
    random.seed()
    no_dcells = random.randint(0,2)
    dcells = random.sample([0,1,2,3],no_dcells)
    for cell in dcells:
        r = cell/2
        c = cell - r*2
        state[r,c] = 1
    return state
