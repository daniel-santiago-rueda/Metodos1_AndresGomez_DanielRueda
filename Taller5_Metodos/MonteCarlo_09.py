import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def f(points):

    return (2**-7)*(np.sum(points, axis=0))**2

def get_points(n):
    x = np.random.uniform(0, 1, size=n)
    x2 = np.random.uniform(0, 1, size=n)
    x3 = np.random.uniform(0, 1, size=n)
    x4 = np.random.uniform(0, 1, size=n)
    x5 = np.random.uniform(0, 1, size=n)
    x6 = np.random.uniform(0, 1, size=n)
    x7 = np.random.uniform(0, 1, size=n)
    x8 = np.random.uniform(0, 1, size=n)

    return x, x2, x3, x4, x5, x6, x7, x8

N = int(1e7)
sample = f(get_points(N))

integral = np.average(sample)

print("Para la aproximación se utilizaron 10^7 puntos.\n")
print("Valor exacto: " + str(25./192.) + "\n" + "Valor aproximado sin tomar en cuenta precisión: "\
    + str(integral) + "\n" + "Valor aproximado con las tres cifras de precisión: " + str(integral)[:5])
