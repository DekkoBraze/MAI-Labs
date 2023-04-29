import matplotlib.pyplot as plt
import math
import numpy as np

space = np.linspace(0,12*math.pi, 2000)
x = []
y = []
z = []
k = []

lin = math.sin(55)
for t in space:
    x.append(math.sin(t)*(math.e**math.cos(t) - 2 * math.cos(4*t) + math.sin(t/12)**5))
    y.append(math.cos(t)*(math.e**math.cos(t) - 2 * math.cos(4*t) + math.sin(t/12)**5))
    z.append(x[-1]*lin)
    k.append(y[-1]*lin)

plt.plot(x, y)
plt.plot(z, k)

plt.show()