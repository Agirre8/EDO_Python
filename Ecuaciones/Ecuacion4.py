from Importaciones.importaciones import *

def dF3(y,x):
    dy3 = sympy(3*t**2+y)/(2*t)
    return dy3

sol3 = odeint(dF3,x)

plt.figure()
plt.plot(x,sol3)
plt.grid()
plt.show()


