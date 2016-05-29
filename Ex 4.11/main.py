from agent_program import AgentProgram

e = int(raw_input())
graph = {}

for i in range(e):
    ip = map(int,raw_input().split())
    n1,n2,w = ip[0],ip[1],ip[2]
    if not n1 in graph.keys():
        graph[n1] = {}
    graph[n1][n2] = w
    if not n2 in graph.keys():
        graph[n2] = {}
    graph[n2][n1] = w

s = int(raw_input())

AgentProgram(graph=graph,start_city=s)


