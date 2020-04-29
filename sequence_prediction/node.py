class Node:
    def __init__(self,domain,parent=None,isLeafNode=True,\
            domain_ptr=0,lchild=None,rchild=None):
        self.domain = domain
        self.parent = parent
        self.isLeafNode = isLeafNode
        self.domain_ptr = domain_ptr
        self.lchild = lchild
        self.rchild = rchild
        
    
