import copy
def ValidateAction(state,action):
    nstate = copy.deepcopy(state)
    if state[2] == 0: #people incoming
        nstate[0] += action[0]
        nstate[1] += action[1]
        if nstate[0] > 3 or nstate[1] > 3:
            return False
        if (nstate[0] == 1 or nstate[0] == 2) and \
                           nstate[0] != nstate[1]:
            return False
    else: #people outgoing
        nstate[0] -= action[0]
        nstate[1] -= action[1]
        if nstate[0] < 0 or nstate[1] < 0:
            return False
        if (nstate[0] == 1 or nstate[0] == 2) and \
                           nstate[0] != nstate[1]:
            return False
    return True
        
        
