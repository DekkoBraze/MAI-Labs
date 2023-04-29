import pandas as pd
from scipy.signal import argrelmin
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

df = pd.read_csv("sample_trajectory.txt", header=None, sep="\s+", names=['t', 'x', 'y', 'z', 'x_dot', 'y_dot', 'z_dot'])

x = list(df['x'])
y = list(df['y'])
z = list(df['z'])

def distance(x, y, z):
    dis = np.sqrt(np.square(x) + np.square(y) + np.square(z))
    return dis

# Находим массив расстояний между точками кривой и исходной
dis = distance(x, y, z)
# Ищем массив индексов минимальных элементов
min_idxs = argrelmin(dis)[0]
# Ищем в этом массиве минимальный индекс
glob_min_idx = min_idxs[np.argmin(dis[min_idxs])]
# Находим минимальный x, y и искомое расстояние
min_x = x[glob_min_idx]
min_y = y[glob_min_idx]
min_d = dis[glob_min_idx]
print("Answer:", min_d)

# Для fminbound требуется функция, которая содержит один аргумент для проверки, однако в нашей функции их 3, т е fminbound неприменима к функции distance
# Пример правильного использования fminbound - нашли значение аргумента в заданном интервале, при котором функция выдает минимальный результат
def f(x):
    return (x-1)**2
minimizer = op.fminbound(f, -4, 4)
print(minimizer)