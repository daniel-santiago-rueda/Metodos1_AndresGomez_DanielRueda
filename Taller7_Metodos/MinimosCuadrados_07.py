import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

data = np.loadtxt('Taller7_Metodos\Data\Sigmoid.dat', skiprows=1, delimiter=',')

x = data[:,0]
y = data[:,1]
N = len(x)

def model(x, theta):

    return theta[0]/(theta[1]+np.exp(-theta[2]*x))

def chi(theta, x, y):

    return y-model(x, theta)

def grad(x, theta, h=1e-7):

    return np.array([1/(theta[1]+np.exp(-theta[2]*x)),\
                    -(theta[0]/(theta[1]+np.exp(-theta[2]*x))**2),\
                    (np.exp(-theta[2]*x)*theta[0]*x)/(theta[1]+np.exp(-theta[2]*x))**2])

def chic(theta, x, y):

    return np.sum((y-model(x, theta))**2)

def get_parameters(x, y, lr=1e-3, epochs=int(1e4), error=1e-2):
    d = 1
    it = 0
    next_pt = np.array([1, 1, 1])

    while d > error and it < epochs:
        CurrentF = chic(next_pt, x, y)

        #Machine Learning
        grad_desc = chi(next_pt, x, y)*grad(x, next_pt)
        next_pt = np.subtract(next_pt, lr*(-2*np.array([np.sum(grad_desc[0]), np.sum(grad_desc[1]), np.sum(grad_desc[2])])))

        NewF = chic(next_pt, x, y)
        d = np.abs( CurrentF - NewF )/NewF

        it += 1

    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)

    if it == epochs:
        print(' Entrenamiento no completado ')

    return next_pt

parameters = get_parameters(x, y)

t = np.linspace(np.min(x),np.max(x),50)
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.scatter(x, y, c='r', label='Datos Originales')
xsym = sym.Symbol('x',real=True)
ax.plot(t, model(t, parameters), label='Best Fit Model:\n' + str(parameters[0]/(parameters[1]+sym.exp(-parameters[2]*xsym))))
ax.legend(prop = {'size' : 7}, loc = 'upper left')
plt.show()
