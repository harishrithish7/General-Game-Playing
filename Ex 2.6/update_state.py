def UpdateState(agent,state,action):
    if action == "SUCK UP DIRT":
        state[agent.posx,agent.posy] = 0
