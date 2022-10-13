from cmath import exp
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import sympy


#y` = e^(-3x)-2y
#y` = x^2y-y/1+y
def dF(y,x):
    dy = sympy(x**2*y-y)/(1+y)
    return dy
#Expresamos una ecuacion algebraica cualquiera

y0=-1
x0=3
x = np.linspace(0,5,100)

sol = odeint(dF,y0,x0,x)

plt.figure()
plt.plot(x,sol)
plt.grid()
plt.show()


def dF1(y,x):
    dy1 = sympy(y*log(y))/(sin(x))
    return dy1

y01=exp
x01=pi/2

sol1 = odeint(dF1,y01,x01,x)

plt.figure()
plt.plot(x,sol1)
plt.grid()
plt.show()


def dF2(y,x):
    dy2 = sympy(2*(t-2)**2*(y/(t-2)))
    return dy2

sol2 = odeint(dF2,x)

plt.figure()
plt.plot(x,sol2)
plt.grid()
plt.show()

def dF3(y,x):
    dy3 = sympy(3*t**2+y)/(2*t)
    return dy3

sol3 = odeint(dF3,x)

plt.figure()
plt.plot(x,sol3)
plt.grid()
plt.show()


