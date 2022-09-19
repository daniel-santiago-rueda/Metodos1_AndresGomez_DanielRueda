import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

#Código taller 3 para encontrar raíces de polinomios de Laguerre
def GetLaguerre(n):
    '''Calcula el n-ésimo polinomio de Laguerre haciendo uso de la
    fórmula de rodrigues.
    '''
    x = sym.Symbol('x', Real=True)
    y = sym.Symbol('y', Real=True)

    y = sym.exp(-x)*x**n
    p = sym.exp(x)*sym.diff(y, x, n)/(np.math.factorial(n))
    #derivada enesima de y con respecto a x

    return sym.lambdify([x], p, 'numpy'), p

def GetRootsLaguerre(f, df, xn, itmax=1000, precision = 1e-5):
    '''
    Calcula las raíces de un polinomio de Laguerre partiendo de un punto xn
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

def GetAllRoots(n, tol=5):
    x_trial = np.linspace(0, 100, 300)
    roots = np.array([])
    poly,p = GetLaguerre(n)
    x = sym.Symbol('x', Real=True)
    df = sym.diff(p, x, 1)
    derivative = sym.lambdify([x], df, 'numpy')

    for i in x_trial:
        root = GetRootsLaguerre(poly, derivative, i)
        croot = np.round(root, tol)
        if croot not in roots:
            roots = np.append(roots, croot)
    roots.sort()

    return roots

#Punto A
def f(x): return (np.exp(x)*x**3)/(np.exp(x)-1)

def calculate_weight(n, root, L_np1):

    return root/((n+1)**2*(L_np1(root))**2)

def gauss_laguerre_quadrature(n = 3, tolerance=8):
    roots = GetAllRoots(n, tol=tolerance)
    weights = calculate_weight(n, roots, GetLaguerre(n+1)[0])
    function_values = f(roots)

    integral = np.sum(weights*function_values)

    return round(integral, tolerance)

#Se imprime el resultado final del punto A
print("El valor de la integral con n = 3 y tolerancia de 8 cifras decimales es " + str(gauss_laguerre_quadrature()))

#Punto B
def gauss_laguerre_quadrature_error(n, tolerance=8): #tolerance máximo es 8 por precisión de GetRootsLaguerre()
    errors = np.array([])
    for value in n:
        errors = np.append(errors, gauss_laguerre_quadrature(n=value, tolerance=tolerance)/(np.pi**4/15))

    return errors

n = np.linspace(2, 10, 9, dtype=int)
errors = gauss_laguerre_quadrature_error(n)

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(n, errors, label= "Laguerre Quadrature Accuracy", color='b')
ax.legend(loc='lower right')
ax.set_ylabel("Error")
ax.set_xlabel("n")
ax.grid()
ax.set_axisbelow(True)

plt.show()
