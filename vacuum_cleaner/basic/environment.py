from agent_user import Program
from get_percept import GetPercept
from validate_action import ValidateAction
from update_score import UpdateScore
from update_state import UpdateState

def Environment(state,agent):
    score = 0
    while True:
        print state
        percept = GetPercept(state=state,agent=agent)
        action = Program(percept)
        while not ValidateAction(agent=agent,action=action,state=state):
            print "Invalid Action"
            action = Program(percept)
        UpdateState(agent=agent,state=state,action=action)
        agent.UpdatePosition(action)
        score = UpdateScore(score=score,action=action)
        print action,score
        if action == "TURN OFF":
            break
    return score
    
