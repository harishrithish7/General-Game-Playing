from possible_action import PossibleAction
from new_node import NewNode

def ExpandFringe(fringe,node,depth):
    if node.depth >= depth:
        return
    actions = PossibleAction(node)
    for action in actions:
        new_node = NewNode(node=node,action=action)
        fringe.insert(0,new_node)
