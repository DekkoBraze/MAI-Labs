import matplotlib.pyplot as plt
import random as rnd
import numpy as np
import cmath as cm

o = []
w = []
e = 0
for i in range(100):
    o.append(rnd.uniform(0, 1.5))
    #w.append(rnd.uniform(1, 2.5))

w = 2*e - np.square(o)
w = np.array(list(map(cm.sqrt, w)))

ctr = plt.plot(o, w.imag)
plt.show()
