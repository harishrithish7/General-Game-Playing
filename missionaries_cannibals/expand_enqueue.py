from validate_action import ValidateAction
import copy
from node import Node
def ExpandEnqueue(q,node):
    actions = [[1,0],[0,1],[1,1],[2,0],[0,2]]
    for action in actions:
        if ValidateAction(state=node.state,action=action):
            nstate = copy.deepcopy(node.state)
            naction = copy.deepcopy(action)
            if node.state[2] == 0: #people incoming
                nstate[0] += action[0]
                nstate[1] += action[1]
            else: #people outgoing
                nstate[0] -= action[0]
                nstate[1] -= action[1]
                action *= -1
            nstate[2] = 1-nstate[2]
            new_node = Node(state=nstate,parent=node,depth=\
                        node.depth+1,path_cost=0,action=naction)
            q.append(new_node)
            
            
            
    
