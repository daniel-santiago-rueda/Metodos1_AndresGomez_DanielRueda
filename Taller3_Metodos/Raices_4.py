import numpy as np
import sympy as sym
from matplotlib import rc
import matplotlib.pyplot as plt

def GetLegendre(n):
    '''Calcula el n-ésimo polinomio de Legendre haciendo uso de la
    fórmula de rodrigues.
    '''
    x = sym.Symbol('x', Real=True)
    y = sym.Symbol('y', Real=True)

    y = (x**2-1)**n
    p = sym.diff(y, x, n)/(2**n*np.math.factorial(n))
    #derivada enesima de y con respecto a x
    return sym.lambdify([x], p, 'numpy'), p

def GetRootsLegendre(f, df, xn, itmax=1000, precision = 1e-5):
    '''
    Calcula las raíces de un polinomio de Legendre partiendo de un punto xn
    '''
    error = 1
    it = 0
    while error>precision and it<itmax:
        try:
            xn1 = xn - f(xn)/df(xn)
            error = np.abs(f(xn)/df(xn))
        except ZeroDivisionError:
            print('División por cero')
        xn = xn1
        it += 1
    if it == itmax:
        return False
    else:
        return xn

def GetAllRoots(n, tol=6):
    x_trial = np.linspace(-1, 1, 200)
    roots = np.array([])
    poly,p = GetLegendre(n)
    x = sym.Symbol('x', Real=True)
    df = sym.diff(p, x, 1)
    df = sym.lambdify([x], df, 'numpy')
    for i in x_trial:
        root = GetRootsLegendre(poly, df, i)
        croot = np.round(root, tol)
        if croot not in roots:
            roots = np.append(roots, croot)
    roots.sort()

    return roots

n = int(input("Ingrese el grado del polinomio de Legendre al cual le quiere \"sacar las raíces\": "))
roots = GetAllRoots(n)
print("\nLas " +str(n)+" raíces del polinomio de grado "  + str(n) + " de Legendre son: ")
for root in roots:
    print(str(root))

