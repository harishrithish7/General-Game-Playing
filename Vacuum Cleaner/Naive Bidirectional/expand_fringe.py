from possible_action import PossibleAction
from new_node import NewNode
from minimal_node import MinimalNode

def ExpandFringe(fringe,node,depth,visited_nodes):
    if node.depth >= depth:
        return
    actions = PossibleAction(node)
    for action in actions:
        new_node = NewNode(node=node,action=action)
        minimal_node = MinimalNode(state=new_node.state,\
                    posx=new_node.posx,posy=new_node.posy,\
                    orientation=new_node.orientation)
        
        if (not minimal_node in visited_nodes) or \
           new_node.action=="TURN OFF":
            visited_nodes[minimal_node] = new_node.path_cost
            fringe.insert(0,new_node)

        elif new_node.path_cost > visited_nodes[minimal_node]:
            visited_nodes[minimal_node] = new_node.path_cost
            fringe.insert(0,new_node)
