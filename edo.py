import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

#y`+2y = e^(-3x)
def dF(y,x):
    dy = np.exp(-3*x)-2*y
    return dy

y0=[1,2,3]
x = np.linspace(0,5,100)

sol = odeint(dF,y0,x)

plt.figure()
plt.plot(x,sol)
plt.grid()
plt.show()

