import numpy as np
import math
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([[0., 0], [0, 1], [1, 0], [1, 1]])
# Радиус и координаты окружности
circle = (0.3, [0.5, 0.5])

# X левого края окружности (будем с этой точки вести цикл)
x = circle[1][0]-circle[0] 

# Создаем массив точек окружности по x
while x <= circle[0]+circle[1][0]:
    # Увеличиваем вместимость массива на 2
    points = np.resize(points, [points.shape[0]+2, 2])
    # К вектору, который представляет собой разницу между исходным радиусом и радиусом с измененным ходом прибавляем х центра
    v = math.sqrt(circle[0]**2-(x-circle[1][0])**2)
    y1 = v+circle[1][0]
    y2 = circle[1][0]-v
    # Добавляем новые точки в массив
    points[points.shape[0]-2] = [x, y1]
    points[points.shape[0]-1] = [x, y2]
    # Определяем один шаг
    x += 0.01

# Триангуляция
tri = Delaunay(points)
# Формируем треугольники
simp = tri.simplices
index = [0, 1, 2, 3]
new_simplices = np.array([simp[0]])

# Удаляем треугольники внутри круга
for i in range(1, simp.shape[0]):
    for j in range(3):
        if simp[i][j] in index:
            new_simplices = np.resize(new_simplices, [new_simplices.shape[0]+1, 3])
            new_simplices[new_simplices.shape[0]-1] = simp[i]
            break

# Отображение
plt.triplot(points[:,0], points[:,1], new_simplices)
plt.plot(points[:,0], points[:,1], 'o')

# 3.1 - Центры и площади
centers = np.zeros([len(new_simplices), 2])
squares = []
for tr in range(0, len(new_simplices)):
    coordinates = np.array([[1.,1.], [1.,1.], [1.,1.]])
    center = [0., 0.]
    for i in range(0, 3):
        coordinates[i][0] = points[new_simplices[tr][i]][0]
        coordinates[i][1] = points[new_simplices[tr][i]][1]
        center[0] = center[0] + points[new_simplices[tr][i]][0]
        center[1] = center[1] + points[new_simplices[tr][i]][1]
    # Определяем площадь треугольника (по координатам вершин)
    squares.append(0.5*abs((coordinates[1][0]-coordinates[0][0])*(coordinates[2][1]-coordinates[0][1])-(coordinates[2][0]-coordinates[0][0])*(coordinates[1][1]-coordinates[0][1])))
    center[0] = center[0]/3
    center[1] = center[1]/3
    centers[tr][0] = center[0]
    centers[tr][1] = center[1]

print("Squares:")
print(squares)
print("Centers:")
print(centers)

plt.plot(centers[:,0], centers[:,1], 'o')   
plt.axis('square')
plt.show()