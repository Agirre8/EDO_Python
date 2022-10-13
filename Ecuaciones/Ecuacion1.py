
from cmath import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import sympy

def dF(y,x):
    dy = (x**2*y-y)/(1+y)
    return dy

#Expresamos una ecuacion algebraica cualquiera

y0=-1

t = np.linspace(0,5)

def solucion():
    y = odeint(dF,y0,t)

    plt.figure()
    plt.plot(t,y)
    plt.grid()
    plt.show()

solucion()




