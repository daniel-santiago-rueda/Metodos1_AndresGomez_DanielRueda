import numpy as np

class LinearSystemSolver:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def GetJAcobiMethod(self, itmax=1000, error=1e-10):
        filas_a = np.size(self.A, 0)
        columnas_a = np.size(self.A, 1)
        x = np.zeros(columnas_a)
        sumk = np.zeros_like(x)        
        it = 0
        residuo = np.linalg.norm(self.b - np.dot(self.A,x))
        while (residuo > error and it < itmax):
            it += 1
            for i in range(filas_a):
                sum_ = 0
                for j in range(columnas_a):
                    if i != j:
                        sum_ += self.A[i][j]*x[j]
                sumk[i] = sum_
            for i in range(filas_a):
                if self.A[i,i] != 0:
                    x[i] = (self.b[i] - sumk[i])/self.A[i,i]
                else:
                    print('No fue posible determinar la solución.')
            residuo = np.linalg.norm(self.b - np.dot(self.A,x))
        return x, it

    def GetGaussSeidelMethod(self, itmax=1000, error=1e-10):
        filas_a = np.size(self.A, 0)
        columnas_a = np.size(self.A, 1)
        x = np.zeros(columnas_a)
        sumk = np.zeros_like(x)
        it = 0
        residuo = np.linalg.norm(self.b - np.dot(self.A,x))
        while (residuo > error and it < itmax):
            it += 1
            for i in range(filas_a):
                sum_ = 0
                for j in range(columnas_a):
                    if i!=j:
                        sum_ += self.A[i][j]*x[j]
                    sumk[i]=sum_
                    if self.A[i][i] != 0:
                        x[i] = (self.b[i] - sumk[i])/self.A[i,i]
                    else:
                        print('No fue posible determinar la solución.')
            residuo = np.linalg.norm(self.b-np.dot(self.A,x))
        return x, it

A = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])

LinearSystem = LinearSystemSolver(A, b)
Jacobi_sol, Jacobi_it = LinearSystem.GetJAcobiMethod()
GaussSeidel_sol, GaussSeidel_it = LinearSystem.GetGaussSeidelMethod()

print('Usando el metodo de Jacobi, se encontró la solución {} en {} iteraciones'.format(Jacobi_sol, Jacobi_it))
print('Usando el metodo de Gauss-Seidel, se encontró la solución {} en {} iteraciones'.format(GaussSeidel_sol, GaussSeidel_it))

