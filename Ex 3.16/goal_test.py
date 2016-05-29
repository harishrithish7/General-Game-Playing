from evaluate import Evaluate

def GoalTest(root,seq):
    for i,num in enumerate(seq):
        if num != Evaluate(node=root,n=i):
            return False
    return True
