import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

N = int(10**4)
x = np.random.uniform(0,100,N)

def Correlations(k):
    sum_ = 0
    for i in range(N):
        sum_ += (x[i]*x[i+k])
        return sum_/N

k = np.array(range(0, 30))
for i in k:
    print(Correlations(i))
