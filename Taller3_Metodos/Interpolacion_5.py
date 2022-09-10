import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os.path as path
import wget


file = 'InterpolacionNewtonNoequi.csv'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv'
if not path.exists(file):
    Path_ = wget.download(url, file)
else:
    Path_ = file

Data = pd.read_csv(Path_, sep=',')

X = np.float64(Data['X'])
Y = np.float64(Data['Y'])

def NewtonGregoryNoequi(X, Y, x):    
    '''
    Calcula el polinomio de interpolación de Newton-Gregory para 
    puntos no equidistantes.
    '''
    Sum_ = Y[0]   
    poly = 1.0
    slope = 0.0
    
    for i in range(1, len(X)):
        poly *= (x-X[i-1])
        slope = GetSlope(X,Y,i-1,i)
        Sum_ += poly*slope
    return Sum_

def GetSlope(X, Y, deg, step):
    '''
    Retorna el valor de la pendiente para un factor del polinomio interpolador.
    '''
    if deg==0:
        return (Y[step]-Y[step-1])/(X[step]-X[step-1])
    else:
        return (GetSlope(X,Y,deg-1,step)-GetSlope(X,Y,deg-1,step-1))/(X[step]-X[step-deg-1])


x = np.linspace(np.min(X), np.max(X), 100)
y = NewtonGregoryNoequi(X,Y,x)

plt.scatter(X,Y, color='r', label= "Datos")
plt.plot(x,y, label = "Interpolación")
plt.legend(loc='upper left')
plt.show()

