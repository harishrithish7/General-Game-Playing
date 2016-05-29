from agent_program import AgentProgram

node = AgentProgram()
while node != None:
    print node.state
    node = node.parent
