from math import factorial
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

alfa = 2
beta = 4
Npoints = 10000

def Gamma(a):
    return factorial(a-1)

def f(x):
    return ( Gamma(alfa+beta) )/( Gamma(alfa)*Gamma(beta) )*(x**(alfa-1))*((1-x)**(beta-1))

maximum = 135/64

x = np.random.uniform(0, 1, Npoints)
y = np.random.uniform(0, maximum, Npoints)

valid_points = 0
for i in tqdm(range(Npoints)):
    if y[i]<f(x[i]):
        valid_points+=1

integral = maximum * valid_points/Npoints
error = np.abs(1-integral)

print(f"La integral de la función es {integral}")
print(f"El error porcentual de esta estimación es {round(error*100,3)}%")

