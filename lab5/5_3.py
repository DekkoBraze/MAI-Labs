import pandas as pd
from scipy.signal import argrelmin
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy

df = pd.read_csv("sample_trajectory.txt", header=None, sep="\s+", names=['t', 'x', 'y', 'z', 'x_dot', 'y_dot', 'z_dot'])

t = list(df['t'])
x = list(df['x'])
y = list(df['y'])
z = list(df['z'])
x_dot = list(df['x_dot'])
y_dot = list(df['y_dot'])
z_dot = list(df['z_dot'])

def distance(i, x, y, z):
    i = round(i)
    x = x[i]
    y = y[i]
    z = z[i]
    dis = np.sqrt(np.square(x) + np.square(y) + np.square(z))
    return dis

# Функция находит пройденный путь относительно радиус-вектора
#def distance(t, x, y, z, x_dot, y_dot, z_dot):
#    # Вектор скорости
#    v1 = [x_dot, y_dot, z_dot]
#    # Радиус-вектор точки
#    v2 = [-x, -y, -z]
#    # Находим проекцию вектора скорости на радиус вектор. np.dot - скалярное произведение
#    v3 = np.dot(v1, v2) / np.linalg.norm(v2)
#    dis = scipy.integrate.quad(v3, 0, t)
#    return dis

# Находим массив расстояний между точками кривой и исходной
dis = []
for i in range(len(x)):
    d = distance(i, x, y, z)
    dis.append(d)
dis = np.array(dis)
print(dis)
# Ищем массив индексов минимальных элементов
min_idxs = argrelmin(dis)[0]
# Ищем в этом массиве минимальный индекс
glob_min_idx = min_idxs[np.argmin(dis[min_idxs])]
# Находим минимальный x, y и искомое расстояние
min_x = x[glob_min_idx]
min_y = y[glob_min_idx]
min_d = dis[glob_min_idx]
print("Answer:", min_d)
# Найти точнее, проинтегрировав - в интернете ничего не нашел

# Для fminbound требуется функция, которая содержит один аргумент для проверки, однако в нашей функции их 3, т е fminbound неприменима к функции distance
# Пример правильного использования fminbound - нашли значение аргумента в заданном интервале, при котором функция выдает минимальный результат
def f(x):
    return (x-1)**2
minimizer = op.fminbound(distance, args = (x, y, z), x1=-4, x2=4)
print('Min = ', distance(round(minimizer), x, y, z))
# Создать функцию одного аргумента, которая будет перебирать x, y, z
# Одномерная минимизация функции distance по каждому аргументу в итоге даст результат [0, 0, 0] с r = 0