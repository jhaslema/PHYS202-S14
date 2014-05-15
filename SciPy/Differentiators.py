
import numpy as np

def twoPtForwardDiff(x,y):
    """returns the derivative of y with respect to x using the two point forward differentiation method
    this method consists of taking the value at y=x and the value at y=x+1 and finding the difference 
    between them then dividing by the difference in x"""
    dydx1 = np.zeros(y.shape,float)

    dydx1[0:-1] = np.diff(y)/np.diff(x)
    dydx1[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx1

def twoPtCenteredDiff(x,y):
    """returns the derivative of y with respect to x using the two point centered differentiation method
    this method consists of taking the value at y=x-1 and the value at y = x+1 and finding the difference
    between them dividing by the difference in x"""
    dydx2 = np.zeros(y.shape,float) #we know it will be this size
    dydx2[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) #center difference
    dydx2[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx2[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    return dydx2

def fourPtCenteredDiff(x,y):
    """Uses a four point centered differentiation method in order to calculate the derivative of y with respect to x"""
    dydx2 = np.zeros(y.shape,float)
    dydx2[2:-2] = (y[0:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(12*(x[1] - x[0]))
    dydx2[1] = (y[2] - y[1])/(x[2] - x[1])
    dydx2[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    dydx2[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx2[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx2