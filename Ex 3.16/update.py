def Update(node):
    if node == None:
        return False
    if Update(node.lchild) == False:
        if Update(node.rchild) == False:
            node.domain_ptr = (node.domain_ptr+1)%\
                                            len(node.domain)
            if node.domain_ptr == 0:
                  return False
    return True
            
                                  
