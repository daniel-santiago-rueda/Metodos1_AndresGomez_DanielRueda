import numpy as np
import matplotlib.pyplot as plt
import sympy as sy


X = np.linspace(0.1, 1.1, 100)

def func(x): return np.sqrt(np.tan(x))
h = X[1]-X[0]

#Punto c
def derivada_progresiva(f, x, h):
    return (1/(2*h))*(-3*f(x)+4*f(x+h)-f(x+2*h))

derv_progresiva = derivada_progresiva(func, X,h)
#Punto d
def derivada_central(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)

derv_central = derivada_central(X, func, h)

#Punto e
def derivada_exacta(x):
    return 1/(2*(np.cos(x)**2)*(np.tan(x)**0.5))

derv_exacta = derivada_exacta(X)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(2,4,1)
ax1 = fig.add_subplot(2,4,2)
ax2 = fig.add_subplot(2,4,3)
ax3 = fig.add_subplot(2,4,4)
ax4 = fig.add_subplot(2,4,5)
ax5 = fig.add_subplot(2,4,6)

ax.plot(X, derv_central)
ax.set_title("Derivada Central")

ax1.plot(X, derv_progresiva)
ax1.set_title("Derivada Progresiva")

ax2.plot(X, derv_exacta)
ax2.set_title("Derivada Exacta")

ax3.plot(X, derv_central)
ax3.plot(X, derv_exacta)
ax3.plot(X, derv_progresiva)
ax3.set_title("Las Tres Derivadas")

#Punto F
error_progresiva = np.abs(derv_exacta-derv_progresiva)

error_central = np.abs(derv_exacta-derv_central)

ax4.plot(X, error_central)
ax4.set_title("Error Derivada Central")

ax5.plot(X, error_progresiva)
ax5.set_title("Error Derivada Progresiva")

plt.show()

#Conclusión punto F: Las derivadas tienen el mismo orden de precisión por el comportamiento de sus errores nodales en las gráficas.