import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

n = 10
m = 2

X = np.arange(n)
Y = np.arange(n)

# Функция делает  матрицу со значениями, которые равны сумме значений столбца и строки (детальнее - возвращает массив с рангом
# который является суммой рангов двух массивов)
res = np.add.outer(X, Y) % 2
# Создаем фигуру м на м
# subplots - создает фигуру (fig) и заголовки осей (ax)
fig, ax = plt.subplots(figsize=(m, m))

# imshow - представляет данные в 2D виде
ax.imshow(res, interpolation='nearest', cmap="binary_r")
# масштабирование осей
ax.set_aspect('auto')
# Задает наименования на осях (мы их удаляем)
plt.xticks([])
plt.yticks([])
plt.show()