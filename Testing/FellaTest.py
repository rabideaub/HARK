'''
A testing module for FellaInterp.  Should be deleted before merging into master.
'''

import sys
import os
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))
import numpy as np

from HARKinterpolation import FellaInterp
from HARKutilities import plotFuncs

#X = np.array([0.,1.,2.,3.,4.,5.,6.,7.])
#Y = 2*X
#V = 0.2*X

#X = np.linspace(0,10,21)
#Y = 2*X
#V = X - 0.1*X**2

X = np.linspace(0,20,200)
Y = 2*X
V = 1. + np.sin(X)
W = X
Z = 1. + np.cos(X)

Test = FellaInterp(v0=1.5, control0=0.3, lower_bound=0.0, upper_bound=None)
Test.addNewPoints(X,V,Y,True)
Test.addNewPoints(X,Z,W,True)
Test.makeValueAndPolicyFuncs()

plotFuncs(Test.ValueFunc,0,20)