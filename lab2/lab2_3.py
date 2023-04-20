import numpy as np
ar1 = np.array([1, 2, 3])
ar2 = np.array([5, 10, 15])
ar3 = np.array([ar2 + ar1 * 0, ar2 + ar1 * 1, ar2 + ar1 * 2, ar2 + ar1 * 3, ar2 + ar1 * 4])
print(ar3)