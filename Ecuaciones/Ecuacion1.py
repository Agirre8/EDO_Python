from Importaciones.importaciones import * 

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




