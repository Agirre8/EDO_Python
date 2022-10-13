from Ecuacion1 import *


def dF2(y,t):
    dy2 = sympy(2*(t-2)**2*(y/(t-2)))
    return dy2

def solucion():
    sol = odeint(dF2,t)

    plt.figure()
    plt.plot(t,sol)
    plt.grid()
    plt.show()

solucion()
