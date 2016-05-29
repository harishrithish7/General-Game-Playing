from initialize import Initialize
from goal_test import GoalTest
from update import Update
from random_restart import RandomRestart
import numpy as np

def AgentProgram(N):
    state = Initialize(N)
    total_conflicts = 0
    for col in range(N):
        row = np.where(state[:,col]==1)[0][0]
        conflicts = np.sum(state[row,:])
        k = col-row
        conflicts += np.sum(np.diag(state,k))

        k = N-1-col-row
        conflicts += np.sum(np.diag(np.fliplr(state),k))
        
        conflicts -= 3
        total_conflicts = total_conflicts+conflicts
    col = 0
    no_update = 0
    for i in range(1000):
        if GoalTest(state):
            return total_conflicts
        row = np.where(state[:,col]==1)[0][0]
        total_conflicts = Update(state,col,total_conflicts)
        if no_update == N:
            total_conflicts = RandomRestart(state=state,col=col,\
                            total_conflicts=total_conflicts)
            no_update = 0
        else:
            if row == np.where(state[:,col]==1)[0][0,0]:
                no_update += 1
            else:
                no_update = 0
        col = (col+1)%N
    return total_conflicts
    
print AgentProgram(20)


