import numpy as np
from matplotlib import pyplot as plt

#definimos la funcion con numpy
def dF(x,y): #y` =f(x,y)
    f = np.exp(-3*x)-2*y
    return f

x0=0
y0=1
xf=5
n=100

h=(xf-x0)/n

x = np.array([x0])#crear una lista para almacenar los resultados
y = np.array([y0])#``


for i in range (1, n+1):
    yn = y0 +h*(dF(x0,y0))
    x0 = x0 + h
    y0 = yn
    x = np.append(x,x0)#ir almacenando al vector x los valores de x0
    y = np.append(y,y0)#ir almacenando al vector y los valores de y0
print(x)
print(y)

plt.figure()#crear el grafico
plt.plot(x,y)
plt.grid()#rejillas en el grafico
plt.show()#print el grafico


