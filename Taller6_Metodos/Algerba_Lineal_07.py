import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

G=(lambda x,y,z,w: x**2+y**2+z**2+w**2-1, 1)

def GetVectorF(G,r):

    v = G[0](r[0],r[1],r[2],r[3])

    return v

def GetJacobian(G,r,h=1e-6):

    J = np.zeros((1,4))

    J[0,0] = (  G[0](r[0]+h,r[1],r[2],r[3]) - G[0](r[0]-h,r[1],r[2],r[3]) )/(2*h)
    J[0,1] = (  G[0](r[0],r[1]+h,r[2],r[3]) - G[0](r[0],r[1]-h,r[2],r[3]) )/(2*h)
    J[0,2] = (  G[0](r[0],r[1],r[2]+h,r[3]) - G[0](r[0],r[1],r[2]-h,r[3]) )/(2*h)
    J[0,3] = (  G[0](r[0],r[1],r[2],r[3]+h) - G[0](r[0],r[1],r[2],r[3]-h) )/(2*h)

    return J.T

def NewtonRaphson(G,r,error=1e-10):

    it = 0
    d = 1
    Vector_d = np.array([])

    while d > error:

        it += 1

        rc = r

        F = GetVectorF(G,r)
        J = GetJacobian(G,r)
        InvJ = np.linalg.inv(J)

        r = rc - np.dot( InvJ, F )

        diff = r - rc

        d = np.linalg.norm(diff)

        Vector_d = np.append( Vector_d , d )

    return r,it,Vector_d

def GetMetric(G,r):
    v = GetVectorF(G,r)

    return np.sqrt(v**2)

def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-9):

    d = 1
    it = 0
    Vector_F = np.array([])

    R_vector = np.array(r)

    while d > error and it < epochs:

        CurrentF = GetMetric(G,r)

        J = GetJacobian(G,r)

        GVector = np.array([GetVectorF(G,r)])
        r -= lr*np.dot(J,GVector)

        R_vector = np.vstack((R_vector,r))

        NewF = GetMetric(G,r)


        Vector_F = np.append(Vector_F,NewF)

        d = np.abs( CurrentF - NewF )/NewF

        it += 1
    """
    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)

    if it == epochs:
        print(' Entrenamiento no completado ')
    """

    return r,it,Vector_F,R_vector

#TODO La graficada no se alcanzó a revisar,
# pero los puntos que saca GetSolve creo que son correctos

X = np.zeros(10**3)
Y = np.zeros(10**3)
Z = np.zeros(10**3)

for i in tqdm(range(10**3)):
    point = np.random.uniform(-1,1,4)
    xsol,it,F,R = GetSolve(G,point,lr=1e-3)

    X[i] = xsol[0]
    Y[i] = xsol[1]
    Z[i] = xsol[2]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')

ax.set_xlim3d(-1.5, 1.5)
ax.set_ylim3d(-1.5, 1.5)
ax.set_zlim3d(-1.5, 1.5)

ax.view_init(10, 60)

ax.scatter(X,Y,Z,color='b')
plt.show()
