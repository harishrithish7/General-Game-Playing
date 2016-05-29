import operator

def Evaluate(node,n):
    if node.isLeafNode:
        return node.domain[node.domain_ptr]
    
    n1 = Evaluate(node.lchild,n)
    n2 = Evaluate(node.rchild,n)
    if n1 == 'n':
        n1 = n
    if n2 == 'n':
        n2 = n
    ops = {'+':operator.add,'-':operator.sub,'*':operator.\
           mul,'/':operator.div,'**':operator.pow}
    if node.domain[node.domain_ptr] == '/' and n2 == 0:
        return float('NaN')

    return ops[node.domain[node.domain_ptr]](n1,n2)
    
