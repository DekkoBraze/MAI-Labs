from scipy.interpolate import RectBivariateSpline
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

with open("sample_surface.txt") as f:
    file_lst = [row.split() for row in f]

cols = file_lst[0]
del file_lst[0]

df = pd.DataFrame(file_lst, columns=cols)

x = df['raan'].to_list()
x = np.array(list(map(int, x)))
y = df['ta'].to_list()
y = np.array(list(map(int, x)))
z = df['dv'].to_list()
z = np.array(list(map(int, x)))

spl2d = RectBivariateSpline(df.index, [0, 1, 2, 3, 4], df)
surf = spl2d(x, y)
def fun(x):
    return spl2d(x[1], x[0])[0, 0]

bnds = ((0, 360), (0, 360))
mn = minimize(fun, (120, 10), bounds=bnds)
print("Answer:", mn.fun)

def jac(f, x, dx=10^-8):
    n = len(x)
    func = f(x)
    jc = np.zeros((n, n))
    for j in range(n): #through columns to allow for vector addition
        Dxj = (abs(x[j])*dx if x[j] != 0 else dx)
        x_plus = [(xi if k != j else xi+Dxj) for k, xi in enumerate(x)]
        jc[:, j] = (f(x_plus)-func)/Dxj
    return jc

res = jac(fun, (0, 0.5))
print("Jacobian example:")
print(res)

#x2,y2 = np.meshgrid(x,y)
#fig = plt.figure()
#ax = Axes3D(fig)
#tri = ax.plot_trisurf(x2.flatten(), y2.flatten(), surf.flatten(), cmap=cm.jet, linewidth=0.1)
#fig.colorbar(tri, shrink=0.5, aspect=5)
##plt.scatter(mn.x[0], mn.x[1], color="green", label="найденный минимум")
#plt.show()