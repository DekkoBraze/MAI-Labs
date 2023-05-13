# import numpy as np
# ar1 = np.array([1, 2, 3])
# ar2 = np.array([5, 10, 15])
# ar3 = np.array([ar2 + ar1 * 0, ar2 + ar1 * 1, ar2 + ar1 * 2, ar2 + ar1 * 3, ar2 + ar1 * 4])
# print(ar3)
import numpy as np
ar1 = np.array([[1, 2, 3], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
ar2 = np.array([[4, 8, 12], [5, 11, 17], [6, 13, 20], [7, 15, 23], [8, 17, 26]])
ar3 = ar1 + ar2
print(ar3) # upd