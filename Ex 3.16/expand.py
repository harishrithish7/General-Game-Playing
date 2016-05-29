from node import Node

def Expand(node,operators):
    if node.isLeafNode:
        node.isLeafNode = False
        lchild = Node(node.domain,parent=node)
        rchild = Node(node.domain,parent=node)
        node.domain = operators
        node.lchild = lchild
        node.rchild = rchild
        return

    Expand(node.lchild,operators)
        
        
