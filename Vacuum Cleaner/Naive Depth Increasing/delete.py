from numpy import *
import numpy as np

a = np.mat(np.zeros((3,3)))
b = np.where(a==0)
print len(b)
if 5 in a:
    print "empty"
else:
    print "Not empty"
