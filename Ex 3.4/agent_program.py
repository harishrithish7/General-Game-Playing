from goal_test import GoalTest
from expand_enqueue import ExpandEnqueue
from node import Node

def AgentProgram():
    root = Node(state=[3,3,1],parent=None,depth=0,\
                path_cost=0,action=None)
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)
        #print node.state
        if GoalTest(node):
            return node #sucess
        ExpandEnqueue(q,node)

    return None #failure
        
    
    

