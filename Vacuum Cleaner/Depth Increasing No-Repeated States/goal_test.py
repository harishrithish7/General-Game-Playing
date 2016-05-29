def GoalTest(node):
    if 1 in node.state:
        return  False
    if node.action == "TURN OFF":
        return True
