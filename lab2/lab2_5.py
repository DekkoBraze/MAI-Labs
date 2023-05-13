import matplotlib.pyplot as plt
import numpy as np
import math as m

r = np.linspace(0, 12 * m.pi, 2000)
x = []
y = []
for t in r:
    x.append(m.sin(t) * (m.e**(m.cos(t)) - 2 * m.cos(4 * t) + m.sin(t / 12) ** 5))
    y.append(m.cos(t) * (m.e**(m.cos(t)) - 2 * m.cos(4 * t) + m.sin(t / 12) ** 5))
plt.plot(x, y)
plt.show() # upd