
import numpy as np

def trapz(func,a,b,N):
    "Performs the trapezoidal integral of func through a and b with a certain number of trapezoids(accuracy, higher the N the more accurate) N"
    h = (b-a)/N
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return I

def simps(func,a,b,N):
    "Performs the Simpson's integral of func through a and b with a certain number of divisions(accuracy, higher the N the more accurate) N"
    h = (b-a)/N
    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())
    return I

def pe(calculated,actual):
    "Returns the percent error given the calculated value and the actual value"
    return (actual-calculated)/actual*100.