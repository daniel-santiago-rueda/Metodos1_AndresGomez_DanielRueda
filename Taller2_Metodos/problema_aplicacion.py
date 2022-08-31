import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 25)
y = x.copy()
h = 0.001

def potencial(x, y):
    return 2*x*(1-(4/(x**2 + y**2)))

def derivada_parcialx(x, y, h):
    return (potencial(x+h, y)-potencial(x-h, y))/(2*h)

def derivada_parcialy(x, y, h):
    return (potencial(x, y+h)-potencial(x, y-h))/(2*h)

def get_campo_velocidades(x, y):
    v_x = np.empty((25, 25))
    v_y = v_x.copy()

    for i in range(25):
        for j in range(25):
            if (x[i]**2 + y[j]**2) > 4:
                v_x[i,j] = round(derivada_parcialx(x[i], y[j], h), 5)
                v_y[i,j] = round(-derivada_parcialy(x[i], y[j], h), 5)

            else:
                v_x[i,j] = 0
                v_y[i,j] = 0

    return v_x, v_y

campo_velocidadesx, campo_velocidadesy = get_campo_velocidades(x, y)

cilindro = np.zeros((1000, 2))
for i in range(1000):
    cilindro[i] = [ 2*np.cos( 2*np.pi*i/1000 ), 2*np.sin( 2*np.pi*i/1000 ) ]

fig = plt.figure(figsize=(6,6))
ejes = fig.add_subplot()
ejes.set_xlabel("x (cm)")
ejes.set_ylabel("y (cm)")
ejes.scatter(cilindro[:,0], cilindro[:,1], color='r', s=1)

for i in range(25):
    for j in range(25):
        ejes.quiver(x[i],y[j],campo_velocidadesx[i,j],campo_velocidadesy[i,j],color='b',alpha=0.7)

plt.show()
