from node import Node
import heapq

def AgentProgram(start_city,graph):
    rem_cities = graph.keys()
    rem_cities.remove(start_city)
    h = MstCost(cities=rem_cities,start_city=start_city,\
                dst=start_city,graph)
    root = Node(state=str(start_city),city=start_city,\
                depth=0,g=0,h=h)
        
    


