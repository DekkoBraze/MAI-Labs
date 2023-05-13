import matplotlib.pyplot as plt
import numpy as np

xAr = np.linspace(0, 15, 50)
yAr = np.linspace(0, 20, 50)
x, y = np.meshgrid(xAr, yAr)
z = (1 / (1 + x ** 2) + 1 / (1 + y ** 2))

fig, ax = plt.subplots()
ctr = plt.contour(x, y, z, levels=4, colors='k')
fil = plt.contourf(x, y, z, levels=60)
plt.title('z = (1 / (1 + x ** 2) + 1 / (1 + y ** 2))')
plt.clabel(ctr)
plt.colorbar(fil)
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.tick_params('both', length=10, width=2, which='major')
plt.show() # upd