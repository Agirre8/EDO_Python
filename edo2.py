from edo import *

def dF(y,x):
    dy = sympy(x**2*y-y)/(1+y)
    return dy