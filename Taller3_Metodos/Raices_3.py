import numpy as np
import sympy as sym

x = sym.Symbol('x', real=True)
f = 3*x**5 + 5*x**4 - x**3

def metodo_newton_raphson(f, Df, xn, itmax=1000, precision=1e-15):
    error = 1
    it=0

    while error > precision and it < itmax:

        try:

            xn_mas1 = xn - f(xn)/Df(xn)
            error = np.abs(f(xn)/Df(xn))

        except ZeroDivisionError:
            print('Error: Division por cero')

        xn = xn_mas1
        it += 1

    if it == itmax:
        return False

    return xn

def calcular_raices(funcion, Df, x_prueba, tolerancia=14):
    raices = np.array([])

    for x in x_prueba:
        raiz = metodo_newton_raphson(funcion, Df, x)

        if raiz != False:
            raiz = np.round(raiz, tolerancia)

            if raiz not in raices:
                if raiz == 0:
                    raiz = 0

                raices = np.append(raices, raiz)

    raices.sort()

    return raices

x_prueba = np.linspace(-10,10,100)
raices = calcular_raices(sym.lambdify(x, f, 'numpy'), sym.lambdify(x, sym.diff(f), 'numpy'), x_prueba)

np.set_printoptions(precision=14)
print(raices)
