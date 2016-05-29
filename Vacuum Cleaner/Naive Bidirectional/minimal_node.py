import numpy as np

def MinimalNode(state,posx,posy,orientation):
    tmp = ''.join(list(np.array(state.astype(str)).reshape(-1)))
    return tmp+'|'+str(posx)+'|'+str(posy)+'|'+\
           str(orientation)    
