def PrintEquation(node):
    if node == None:
        return
    print '(',
    PrintEquation(node.lchild)
    print node.domain[node.domain_ptr],
    PrintEquation(node.rchild)
    print ')',
