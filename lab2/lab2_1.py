import math
import numpy as np
print("Array 1:")
ar1 = np.zeros(11)
for i in range(0, 10):
    ar1[i] = math.pi / 2 ** i
    print(ar1[i])
print(ar1.shape)
print(ar1.nbytes)
print("Array 2:")
ar2 = np.zeros(101)
for i in range(10, 101):
    if (i % 2 == 0):
        ar2[i] = True
    else:
        ar2[i] = False
    print(ar2[i])
print(ar2.shape)
print(ar2.nbytes)
print("Array 3:")
ar3 = np.zeros((10, 10), complex)
for i in range(0, 10):
    for j in range(0, 10):
        ar3[i][j] = complex(1.5 * i, 2.5 * j)
        print(ar3[i][j])
print(ar3.shape)
print(ar3.nbytes)