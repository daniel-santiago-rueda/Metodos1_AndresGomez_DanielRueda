import numpy as np
import matplotlib.pyplot as plt

n = int(input("Ingrese el número (entero) de vueltas que desea que de la espiral: "))

#Calculando 500 valores de r entre [0, 2pi]
r = np.linspace(0, 2*np.pi*n, 500)

#Haciendo cambios de coordenadas, con a=0 y b=1, r=theta
x = r*np.cos(r)
y = r*np.sin(r)

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("Espiral de Arquimedes de " + str(n) + " vueltas")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()