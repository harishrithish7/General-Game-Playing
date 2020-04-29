from copy import deepcopy
from mst_cost import MstCost

class Node:
    def __init__(self,city,g,h,parent=None,state=None,depth=\
             None,rem_cities=None):
        self.city = city
        self.g = g
        self.h = h
        self.f = g+h
        self.parent = parent
        
        self.state = state
        if state == None:
            self.state = parent.state+"-"+str(city)
            
        self.depth = depth
        if depth == None:
            self.depth = parent.depth+1
        
        self.rem_cities = rem_cities
        if rem_cities == None:
            rem_cities = deepcopy(parent.rem_cities)
            rem_cities.remove(city)

        

        

            
        
