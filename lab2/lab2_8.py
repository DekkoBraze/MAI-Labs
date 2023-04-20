import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

n = 8
m = 5

X = np.arange(n)
Y = np.arange(n)

# Функция делает  матрицу со значениями, которые равны сумме значений столбца и строки
res = np.add.outer(X, Y) % 2
# Создаем фигуру м на м
fig, ax = plt.subplots(figsize=(m, m))

ax.imshow(res, interpolation='nearest', cmap="binary_r")
ax.set_aspect('auto')
plt.xticks([])
plt.yticks([])
plt.show()