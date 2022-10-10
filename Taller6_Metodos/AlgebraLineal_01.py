import numpy as np

A = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])

def GetGaussSeidelMethod(A, b, itmax=1000, error=1e-10):
    filas_a = np.size(A, 0)
    columnas_a = np.size(A, 1)
    x = np.zeros(filas_a)
    sumk = np.zeros_like(x)
    it = 0
    residuo = np.linalg.norm(b - np.dot(A,x))
    while ( residuo > error and it < itmax ):
        it += 1
        for i in range(filas_a):
            sum_ = 0
            for j in range(columnas_a):
                if i!=j:
                    print(A[i][j])
                    sum_ += A[i][j]*x[j]
                sumk[i]=sum_
                if A[i][i] != 0:
                    x[i] = (b[i] - sumk[i])/A[i,i]
                    print(x[i])
                else:
                    print('No fue posible determinar la solución.')
        residuo = np.linalg.norm(b-np.dot(A,x))
    return x, it, residuo

Xsol,it,error = GetGaussSeidelMethod(A,b)
print('La solución hallada para el sistema fue {}.\nAdemás se encontró dicha solución en {} iteraciones, y con un error de {}.\n'.format(Xsol, it, error))
