import matplotlib.pyplot as plt
import numpy as np
import math as m

x = np.linspace(0, 100, 100)
y = []

for e in x:
    y.append(2 * m.pi * m.sqrt(e/9.8))
plt.plot(x, y)
plt.show()