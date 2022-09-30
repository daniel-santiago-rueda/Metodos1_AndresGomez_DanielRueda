import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def f(coords):
    x = coords[0]
    y = coords[1]
    z = coords[2]

    return np.exp(np.sqrt(x**2+y**2+z**2))

def get_points(n, r=1):
    X = np.zeros(n)
    Y = np.zeros_like(X)
    Z = np.zeros_like(X)

    for i in tqdm(range(n)):
        u = np.random.rand()

        rho = r*u**(1/3)
        theta = np.random.uniform(0, 2*np.pi)
        phi = np.random.uniform(0, np.pi)

        X[i] = rho*np.cos(theta)*np.sin(phi)
        Y[i] = rho*np.sin(theta)*np.sin(phi)
        Z[i] = rho*np.cos(phi)

    return X, Y, Z

n_ = int(float(input("Ingrese el número de puntos que quiere utilizar para la estimación: ")))
sample = f(get_points(n_))

integral = (4/3)*np.pi*np.average(sample)

print("Valor Aproximado: " + str(integral) + "\n" + "Valor Exacto: " + str(4*np.pi*(np.e-2)))
#TODO preguntar si truncar valor aprox con 1/sqrt(n) y/o se reporta 1/sqrt(n)