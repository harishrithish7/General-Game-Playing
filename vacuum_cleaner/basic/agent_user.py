import copy
class Node:
    def __init__(self,action=None):
        self.action = action
        self.children = [None,None]
        self.suckups = 0

root = Node()
cnode = root

sequences = []
for x in range(512):
    sequences.append("{:09b}".format(x))

for seq in sequences:
    cnode = root
    for idx,percept in enumerate(seq):
        percept = int(percept)
        if cnode.children[percept] != None:
            cnode = cnode.children[percept]
        elif percept == 1:
            if cnode.suckups == 2:
                break
            node = Node("SUCK UP DIRT")
            node.suckups = cnode.suckups+1
            cnode.children[1] = node
            cnode = node
        else:
            if cnode.suckups == 2:
                node = Node("TURN OFF")
                node.suckups = 2
                cnode.children[0] = node
                cnode = node
                break
            elif cnode.suckups == 1:
                if idx in [1,3,5]:
                    node = Node("FORWARD")
                    node.suckups = 1
                    cnode.children[0] = node
                    cnode = node
                elif idx in [2,4]:
                    node = Node("RIGHT")
                    node.suckups = 1
                    cnode.children[0] = node
                    cnode = node
                elif idx == 6:
                    node = Node("TURN OFF")
                    node.suckups = 1
                    cnode.children[0] = node
                    cnode = node
                    break
            elif cnode.suckups == 0:
                if idx in [0,2,4]:
                    node = Node("FORWARD")
                    cnode.children[0] = node
                    cnode = node
                elif idx in [1,3]:
                    node = Node("RIGHT")
                    cnode.children[0] = node
                    cnode = node
                elif idx == 5:
                    node = Node("TURN OFF")
                    cnode.children[0] = node
                    cnode = node
                    break
cnode = root

def Program(percept):
    global cnode
    if percept == 0:
        cnode = cnode.children[0]
    else:
        cnode = cnode.children[1]
    return cnode.action


