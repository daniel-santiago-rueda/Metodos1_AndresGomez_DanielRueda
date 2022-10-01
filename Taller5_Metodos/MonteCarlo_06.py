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

N = int(1e6)
sample = f(get_points(N))

integral = (4/3)*np.pi*np.average(sample)

print("Para la aproximación se utilizaron 10^6 puntos.\n")
print("Valor exacto: " + str(4*np.pi*(np.e-2)) + "\n" + "Valor aproximado sin tomar en cuenta precisión: "\
    + str(integral) + "\n" + "Valor aproximado con las dos cifras de precisión: " + str(integral)[:4])
