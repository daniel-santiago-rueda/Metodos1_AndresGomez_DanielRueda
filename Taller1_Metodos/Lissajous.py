import matplotlib.pyplot as plt
import numpy as np

def graficar_lissajous(nombre_desfase, valor_desfase):
    n_sides = 5
    theta = np.linspace(0,2*np.pi,200)
    fig = plt.figure(figsize=(5,6))
    fig.suptitle("Desfase = " + str(nombre_desfase))

    k = 0
    for n_x in range(1,6):
        angulo_x = n_x*theta
        k += n_x-1
        for n_y in range(n_x,6):
            angulo_y = n_y*theta
            k += 1
            ax1 = fig.add_subplot(n_sides,n_sides,k)
            ax1.plot(np.sin(angulo_x), np.sin(angulo_y + valor_desfase))
            plt.axis('off')

nombres_desfases = np.array(["0", "π/4", "π/2"])
valores_desfases = np.array([0, np.pi/4, np.pi/2])
for i in range(0, 3):
    graficar_lissajous(nombres_desfases[i], valores_desfases[i])

plt.show()
