import numpy as np
import math
print("Задание 1")
ar0 = np.array([60.0, 57.5, 55.0, 52.5, 50.0])
ar = np.array([ar0, ar0 - 12.5 * 1, ar0 - 12.5 * 2, ar0 - 12.5 * 3, ar0 - 12.5 * 4])
c = 0
vib = []
for i in range(5):
    if i != 2:
        for j in range(1, 4):
            vib.append(ar[i][j]) # upd
            c += 1
print(vib)
print("Задание 2")
ar = np.zeros((111,), complex)
lst7 = []
for i in range(0, 11):
    for j in range(0, 11):
        ar[i * 10 + j] = complex(i, j)
        if math.sqrt(i ** 2 + j ** 2) > 7:
            lst7.append((ar[i * 10 + j]))
print(ar)
print(lst7) # upd
