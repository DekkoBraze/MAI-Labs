import numpy as np
import math
print("Задание 1")
ar0 = np.array([60.0, 57.5, 55.0, 52.5, 50.0])
ar = np.array([ar0, ar0 - 12.5 * 1, ar0 - 12.5 * 2, ar0 - 12.5 * 3, ar0 - 12.5 * 4])
c = 0
for i in range(5):
    if i != 2:
        for j in range(1, 4):
            print(ar[i][j])
            c += 1
print("Задание 2")
ar = np.zeros((11, 11), complex)
lst = []
for i in range(0, 11):
    for j in range(0, 11):
        ar[i][j] = complex(i, j)
        if math.sqrt(i**2 + j**2) > 7:
            lst.append(ar[i][j])
for i in lst:
    print(i)

