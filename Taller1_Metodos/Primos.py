import numpy as np
import matplotlib.pyplot as plt

def EsPrimo(n:int): #Confirma si un número es primo o no.
    i = 2
    esPrimo = True
    while i <= np.sqrt(n) and esPrimo:
    #Por un teorema de la Teoría de números, solo es necesario evaluar hasta la raíz de n.
        if np.mod(n, i)==0:
            esPrimo = False
            break
        i+=1
    return esPrimo

#Parte (a)
print("Calculando los primeros 1000 primos...")
primos = []
n=2
while len(primos)<1000:
    if EsPrimo(n):
        primos.append(n)
    n+=1
print("¡Calculados!")

#Parte (b)
print("Los primeros 10 primos son: \n")
for i in range(10):
    print(primos[i])

#Parte (c)
plt.figure(figsize=(8, 5))
plt.plot(range(1000), primos, color='r')
plt.title("Distribución de los primeros 1000 primos")
plt.xlabel("Posición")
plt.ylabel("Primos")
plt.show()