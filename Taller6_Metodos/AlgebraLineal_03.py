from stat import FILE_ATTRIBUTE_SPARSE_FILE
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def MatrixMultiplication(A, B):
    filas_a = np.size(A, 0)
    filas_b = np.size(B, 0)
    columnas_a = np.size(A, 1)
    columnas_b = np.size(B, 1)
    if columnas_a != filas_b:
        return None
    prod = np.empty((filas_a, columnas_b))
    for i in range(filas_a):
        for j in range(columnas_b):
            suma = 0
            for k in range(columnas_a):
                suma += A[i][k]*B[k][j]
            prod[i][j] = suma
    return prod

A = np.array([[1, 0, 0], [5, 1, 0], [-2, 3, 1]])
B = np.array([[4, -2, 1], [0, 3, 7], [0, 0, 2]])

print('\nEl producto de las matrices es:\n')
print(MatrixMultiplication(A, B))


