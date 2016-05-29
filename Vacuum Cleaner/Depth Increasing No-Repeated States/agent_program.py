from node import Node
from expand_fringe import ExpandFringe
from prepare_environment import PrepareEnvironment
from goal_test import GoalTest
from minimal_node import MinimalNode
from possible_action import PossibleAction
import time

def AgentProgram():
    state,posx,posy,orientation = PrepareEnvironment()
    print state
    root = Node(state=state,posx=posx,posy=posy,depth=0,\
                path_cost=0,orientation=orientation)    
    depth = 1
    while True:
        fringe = []
        fringe.append(root)
        visited_nodes = {}
        visited_nodes[MinimalNode(state=state,posx=posx,\
                    posy=posy,orientation=orientation)]=0
        while len(fringe) > 0:
            node = fringe.pop(0)
            """print node.state
            print MinimalNode(state=node.state,posx=node.posx,\
                    posy=node.posy,orientation=node.orientation)
            print node.action,node.posx,node.posy,node.\
                  orientation,node.path_cost"""
            if GoalTest(node):
                return node
            ExpandFringe(fringe=fringe,node=node,depth=depth\
                         ,visited_nodes=visited_nodes)
        depth = depth+1
node = AgentProgram()
while node != None:
    print node.action
    node = node.parent
