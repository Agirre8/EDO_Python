from Ecuacion1 import *


def dF1(y,x):
    dy1 = (y*log(y))/(sin(x))
    return dy1

y01=exp
x01=pi/2

sol1 = odeint(dF1,y01,x01,x)

plt.figure()
plt.plot(x,sol1)
plt.grid()
plt.show()