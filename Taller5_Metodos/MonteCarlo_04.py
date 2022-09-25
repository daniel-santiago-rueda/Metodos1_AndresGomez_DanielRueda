import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

N = 10**4
x = np.random.rand(N)

def Correlations(k):
    sum_ = 0
    for i in range(N-k):
        sum_ += (x[i]*x[i+k])
    return sum_/N

K = np.zeros(30)
Y = np.zeros_like(K)

for i in range(1,31):
    K[i-1] = i
    Y[i-1] = Correlations(i)

plt.plot(K, Y)
plt.title("Generador \'rand\' de Numpy")
plt.xlabel('k-ésimo vecino')
plt.ylabel('C(k)')
plt.ylim((0.2, 0.3))
plt.show()
