import numpy as np

def function(x):
    return 3*x**5 + 5*x**4 - x**3

def central_derivative(f, x, h=1e-7):
    return (f(x+h) - f(x-h))/(2*h)

def metodo_newton_raphson(f, Df, xn, itmax=1000, precision=1e-8):
    error = 1
    it=0

    while error > precision and it < itmax:

        try:
                xn_mas1 = xn - f(xn)/Df(f, xn)
                error = np.abs(f(xn)/Df(f, xn))

        except ZeroDivisionError:
            print('Error: Division por cero')

        xn = xn_mas1
        it += 1

    if it == itmax:
        return False

    return xn

def calcular_raices(f, Df, x_prueba, tolerancia=7):
    raices = np.array([])

    for x in x_prueba:
        raiz = metodo_newton_raphson(f, Df, x)

        if raiz != False:
            raiz = np.round(raiz, tolerancia)

            if raiz not in raices:
                if raiz == 0:
                    raiz = 0

                raices = np.append(raices, raiz)

    raices.sort()

    return raices

x_prueba = np.linspace(-10,10,100)
raices = calcular_raices(function, central_derivative, x_prueba)

np.set_printoptions(precision=15)
print(raices)
