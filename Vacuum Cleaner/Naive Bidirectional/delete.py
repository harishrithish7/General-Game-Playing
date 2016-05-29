import numpy as np
from prepare_environment import PrepareEnvironment
from minimal_node import MinimalNode
from node import Node
from possible_action import PossibleAction

state = np.zeros((2,2),dtype='int32')
posx = 1
posy = 1
orientation = 90
node = Node(state=state,posx=posx,posy=posy,orientation=\
            orientation)
print MinimalNode(state=state,posx=posx,posy=posy,orientation=\
            orientation)
print PossibleAction(node)


