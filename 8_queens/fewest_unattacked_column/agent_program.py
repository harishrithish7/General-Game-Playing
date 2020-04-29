import numpy as np
from node import Node
from goal_test import GoalTest
from expand_node import ExpandNode

def AgentProgram():
    initial_state = np.mat(np.zeros((8,8)))
    root = Node(state=initial_state,depth=0,attacked_cells=\
                initial_state)
    fringe = []
    fringe.append(root)
    expanded_nodes = 0
    while len(fringe) > 0:
        node = fringe.pop(0)
        expanded_nodes = expanded_nodes+1
        if GoalTest(node):
            print node.state
            break
        ExpandNode(fringe=fringe,node=node)
    print expanded_nodes

AgentProgram()
