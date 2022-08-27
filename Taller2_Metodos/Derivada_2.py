import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
function = lambda x: 1/(np.sqrt(1+np.exp(-x**2)))
h = 0.05

#Parte (a), se calcula la derivada central de la función
def CentralDerivative(x, f, h):
    return (f(x+h)-f(x-h))/(2*h)

central_derivative = CentralDerivative(x, function, h)


#Derivada real de la función
real_derivative = lambda x: (x*np.exp(-x**2)) / ((np.sqrt(1+np.exp(-x**2)))**3) 


#Parte (b), se calcula el error local para todos los puntos nodales.
error = np.abs(central_derivative - real_derivative(x))


#Se grafican las partes (a) y (b)
fig = plt.figure(figsize=(13, 5))
ax = fig.add_subplot(1, 2, 1)
ax.plot(x, central_derivative, color='r')
ax.set_title("Derivada central calculada")
ax.set_xlabel("x")
ax.set_ylabel("f\' (x)")
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, error, color = 'orange')
ax2.set_title("Error local en cada punto nodal")
ax2.set_xlabel("x")
ax2.set_ylabel("Error")
plt.show()

