import matplotlib.pyplot as plt
import numpy as np
 
u, v = np.mgrid[0:2 * np.pi:30j, 0:2 * np.pi:30j]
x = (2 + np.sin(v)) * np.cos(u)
y = (2 + np.sin(v)) * np.sin(u)
z = np.cos(v)
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-2, 2)
ax.plot_surface(x, y, z, cmap='inferno')
ax.view_init(elev=90)
plt.show()
# upd