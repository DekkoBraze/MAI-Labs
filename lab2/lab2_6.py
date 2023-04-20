import numpy as np

print("Задание 1")
ar0 = np.array([0, 1, 2, 3, 4, 5])
ar1 = np.array([10, 11, 12, 13, 14, 15])
ar0 = ar0.reshape((2, 3))
ar1 = ar1.reshape((2, 3))
ar = ar0 + ar1
print(ar)
print("Задание 2")
ar0 = np.array([0, 1, 2, 3, 4, 5])
ar0 = ar0[None]





print(ar0)