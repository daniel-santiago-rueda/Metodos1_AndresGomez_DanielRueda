import numpy as np, sympy as sym, matplotlib.pyplot as plt
from matplotlib import cm

#(A)

x = sym.Symbol('x')
y = sym.Symbol('y')

def T(x,y,p):
    a = sym.Symbol('x')
    b = sym.Symbol('y')
    func = 0    
    for i in range(2):
        for j in range(2):
            func += p[2*i+j]*a**j*b**i
    f = sym.lambdify([a,b],func,'numpy')
    return f(x,y)

#(B)

P = np.array([[1,1], [-1,1], [-1,-1], [1,-1]])

#(C)

def interpolation(X, Y):
    A = np.array([[1, X[0], Y[0], X[0]*Y[0]], [1, X[1], Y[1], X[1]*Y[1]], [1, X[2], Y[2], X[2]*Y[2]], [1, X[3], Y[3], X[3]*Y[3]]])
    b = np.array([1, 2, 0.5, 0.3])
    sol = np.linalg.solve(A, b)
    return sol

primera_interpolacion = interpolation(P[:,0], P[:,1])

#(D)

T_vertices = T(P[:,0], P[:,1], primera_interpolacion) 
print( '\nT(1, 1) = {}'.format(T_vertices[0]) )
print( 'T(-1, 1) = {}'.format(T_vertices[1]) )
print( 'T(-1, -1) = {}'.format(T_vertices[2]) )
print( 'T(1, -1) = {}\n'.format(T_vertices[3]) )

#(E)

x, y = np.linspace(-1, 1, 500), np.linspace(-1, 1, 500)
x, y = np.meshgrid(x,y)
Temperatures = T(x, y, primera_interpolacion)

#Superficie 2-D:
surf_2d = plt.pcolormesh(x, y, Temperatures, cmap=cm.coolwarm, shading='auto')
plt.scatter(P[:,0],P[:,1], T(P[:,0],P[:,1],primera_interpolacion), marker='o', color='k')
plt.title('HeatMap Plot 2D')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(surf_2d, orientation='horizontal', label = 'Temperature (K)')

#Superficie 3-D:
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf_3d = ax.plot_surface(x, y, Temperatures, cmap=cm.coolwarm, linewidth=0)
ax.scatter(P[:,0],P[:,1], T(P[:,0],P[:,1],primera_interpolacion),marker='o',color='k',s=50)
ax.set_title('HeatMap Plot 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('T(X,Y)')
fig.colorbar(surf_3d, orientation='horizontal', label = 'Temperature (K)')
plt.show()

#(F)

T_damaged = T(0., 0.5, primera_interpolacion)
print('T(0, 0.5) = {}'.format(T_damaged))

#(G)

def Rotation(theta, x, y):
    rot_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rot_vector = np.dot(rot_matrix, np.array([x, y]))
    return rot_vector.T

#(H)

#Ejemplo de rotacion con 90 grados:
New_P = Rotation(np.pi/2,P[:,0],P[:,1])
New_interpol = interpolation(New_P[:,0],New_P[:,1])
New_T_damaged = T(0.,0.5,New_interpol)
print('Si rotamos el espejo 90 grados, la temperatura del punto dañado es {}'.format(New_T_damaged))

#(I)

theta = np.linspace(0, 2*np.pi, 200)
T_P = np.array([])
for i in theta:
    New_P = Rotation(i,P[:,0],P[:,1])
    New_interpol = interpolation(New_P[:,0],New_P[:,1])
    T_P = np.append(T_P, T(0., 0.5, New_interpol))

Min_T = np.min(T_P)
Theta_min = theta[np.where(T_P==Min_T)]

print('El ángulo que hace que la temperatura en el punto (0, 0.5) sea mínima es theta = {} rad, la temperatura en este punto es {} K'.format(Theta_min[0], Min_T))



