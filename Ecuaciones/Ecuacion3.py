from Ecuacion1 import *


def dF2(y,x,t):
    dy2 = sympy(2*(t-2)**2*(y/(t-2)))
    return dy2

sol = odeint(dF2,dF2.x)

plt.figure()
plt.plot(dF2.x,sol)
plt.grid()
plt.show()
