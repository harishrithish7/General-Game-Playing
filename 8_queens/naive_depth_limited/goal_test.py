import numpy as np

def GoalTest(node):
    state = node.state
    if np.sum(np.sum(state)) != 8:
        return False
    for row in range(8):
        for col in range(8):
            if state[row,col] == 1:
                if np.sum(state[:,col]) != 1:
                    return False
                if np.sum(state[row,:]) != 1:
                    return False

                k = col-row
                if np.sum(np.diag(state,k)) != 1:
                    return False

                k = 7-col-row
                if np.sum(np.diag(np.fliplr(state),k))!=1:
                    return False
    return True
