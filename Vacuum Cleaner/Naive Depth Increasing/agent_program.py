from node import Node
from expand_fringe import ExpandFringe
from prepare_environment import PrepareEnvironment
from goal_test import GoalTest

def AgentProgram():
    state,posx,posy,orientation = PrepareEnvironment()
    print state
    root = Node(state=state,posx=posx,posy=posy,depth=0,\
                path_cost=0,orientation=orientation)
    depth = 1
    while True:
        print depth
        fringe = []
        fringe.append(root)
        while len(fringe) > 0:
            node = fringe.pop(0)
            if GoalTest(node):
                return node
            ExpandFringe(fringe,node,depth)
        depth = depth+1

node = AgentProgram()
while node != None:
    print node.action
    node = node.parent
