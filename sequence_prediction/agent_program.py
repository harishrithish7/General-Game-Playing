from node import Node
from goal_test import GoalTest
from update import Update
from expand import Expand
from print_equation import PrintEquation

def AgentProgram(seq):
    depth = 3
    operators = ['+','-','*','/','**']
    values = [1.0,'n']
    root = Node(domain=operators,isLeafNode=False)
    lchild = Node(domain=values,parent=root)
    rchild = Node(domain=values,parent=root)
    root.lchild = lchild
    root.rchild = rchild

    while True:
        if GoalTest(root=root,seq=seq):
            return root
        if Update(root) == False:
            Expand(node=root,operators=operators)
            depth += 2

seq = [1,3,5]
root = AgentProgram(seq)

PrintEquation(root)

    
