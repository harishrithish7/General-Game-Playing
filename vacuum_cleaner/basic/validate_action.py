def ValidateAction(agent,action,state):
    if action == "FORWARD" and state[agent.posx,agent.posy] not in [0,1]:
        return False
    elif action == "SUCK UP DIRT" and state[agent.posx,agent.posy] != 1:
        return False
    return True
        
