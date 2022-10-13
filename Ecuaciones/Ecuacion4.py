from turtle import end_fill
from Ecuacion1 import *

def dF3(y,t):
    dy3 = sympy(3*t**2+y)/(2*t)
    return dy3


def solucion(t):
    sol = odeint(dF3,t)
    plt.figure()
    plt.plot(t,sol)
    plt.grid()
    plt.show()

solucion()



