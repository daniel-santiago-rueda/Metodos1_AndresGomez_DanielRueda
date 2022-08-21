import matplotlib.pyplot as plt
import numpy as np

#Punto 1
def fibonancci(n):
    if n == 0: return 0

    if n == 1: return 1

    resultado = fibonancci(n-1) + fibonancci(n-2)

    return resultado

datosy = np.zeros(21, dtype=int)
for i in range(0,21):
    fib = fibonancci(i)
    datosy[i] = fib

    print("F_" + str(i) + " = " + str(datosy[i]))

#Punto 2
#En el for loop del punto 1 se creó el array con los datos de Fibonacci
fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(1,2,1)
ax1.plot(datosy, label='Serie Fibonacci')
plt.xticks([0,5,10,15,20])
ax1.legend(loc="upper left")
ax1.set_title("Punto 2")

#Punto 3
AUREO_EXACTO = (1 + 5 ** 0.5) / 2

datosy2 = np.zeros(19)
for i in range(1,20):
    datosy2[i-1] = datosy[i+1]/datosy[i]

ax2 = fig.add_subplot(1,2,2)
ax2.plot(datosy2,label='Estimación usando la serie')
ax2.axhline(y=AUREO_EXACTO,linestyle='--',label='Número Áureo',color='r')
ax2.legend(loc="upper right")
ax2.set_title("Punto 3")

plt.show()
