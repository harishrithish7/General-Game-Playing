import numpy as np

def GoalTest(state):
    N = state.shape[0]
    if np.sum(np.sum(state)) != N:
        return False
    for row in range(N):
        for col in range(N):
            if state[row,col] == 1:
                if np.sum(state[:,col]) != 1:
                    return False
                if np.sum(state[row,:]) != 1:
                    return False

                k = col-row
                if np.sum(np.diag(state,k)) != 1:
                    return False

                k = N-1-col-row
                if np.sum(np.diag(np.fliplr(state),k))!=1:
                    return False
    return True
