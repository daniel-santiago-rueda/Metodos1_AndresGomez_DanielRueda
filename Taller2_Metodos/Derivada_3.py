import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
function = lambda x: 1/(np.sqrt(1+np.exp(-x**2)))
h = 0.05

mascara = [1.0, 0.0, -1.0]

#Se calcula la derivda central en cada punto como una sumatoria de 
#la máscara de convolución por los puntos adyacentes
def CentralDerivative(x, f, h):
    sum = 0
    for i in mascara:
        sum+= f(x-i*h)*i
    return sum/(2*h)

central_derivative_V2 = CentralDerivative(x, function, h)

plt.plot(x, central_derivative_V2, color='g')
plt.title("Derivada central con kernel de convolución")
plt.xlabel("x")
plt.ylabel("f\'(x)")
plt.show()