import matplotlib.pyplot as plt
import numpy as np

xAr = np.linspace(0, 15, 50)
yAr = np.linspace(0, 20, 50)
x, y = np.meshgrid(xAr, yAr)
z = (1 / (1 + x ** 2) + 1 / (1 + y ** 2))

ctr = plt.contour( x, y, z, levels=4, colors='k')
fil = plt.contourf(x, y, z, levels=60)
plt.annotate('Our function', (11, 2), backgroundcolor='w')
plt.clabel(ctr)
plt.colorbar(fil)
plt.show()