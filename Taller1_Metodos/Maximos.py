import numpy as np
import matplotlib.pyplot as plt

archivo = open("Taller1_Metodos/EstrellaEspectro.txt", mode="r")

#El archivo tiene 197 lineas
coords = np.zeros((197,2))

#Se llena la matriz coords
for i in range(197):
    linea = archivo.readline()
    coordinates = linea.split()
    coords[i] = [float(coordinates[0]), float(coordinates[1])]

previous_point = float(coords[0][1])

#Se contaron 41 máximos en la gráfica
maximos = np.zeros((41, 2))
contador_maximos=0

#Se calculan los máximos locales
for i in range(196):
    evaluated_point = float(coords[i][1])
    next_point = float(coords[i+1][1])
    if previous_point < evaluated_point > next_point:
        maximos[contador_maximos]=[float(coords[i][0]), float(coords[i][1])]
        contador_maximos+=1
    previous_point = evaluated_point

x = coords[:,0]
y = coords[:,1]
X = maximos[:,0]
Y = maximos[:,1]

#Se pinta el gráfico junto la señalización de los máximos locales
plt.figure(figsize=(8,5))
plt.title("Máximos")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y)
plt.scatter(X,Y, color='r', s=15)
plt.show()