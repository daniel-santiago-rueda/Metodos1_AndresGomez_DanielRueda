import numpy as np
import pandas as pd
import sympy as sym

def lagrange(x,xi,j):

    prod = 1.0
    n = len(xi)

    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])

    return prod

def Poly(x,xi,yi):

    sum_ = 0.
    n = len(xi)

    for j in range(n):
        sum_ += yi[j]*lagrange(x,xi,j)

    return sum_

data = pd.read_csv('Taller3_Metodos/Parabolico.csv', sep=',')
X = np.float64(data['X'])
Y = np.float64(data['Y'])
x = sym.Symbol('x')

f = Poly(x,X,Y)

f_coefficients = sym.poly(f).coeffs()
lineal_c = float(f_coefficients[1])
quadratic_c = float(f_coefficients[0])

theta = float(sym.atan(lineal_c))
velocity_0 = sym.sqrt(9.8/(2*np.cos(theta)**2*-1*quadratic_c))

theta = round((180/sym.pi)*theta)

print("Velocidad Inicial: " + str(round(velocity_0)) + " m/s\n" + "Ángulo Inicial: " + str(theta) + "°")
