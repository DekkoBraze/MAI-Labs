import matplotlib.pyplot as plt

def is_covered(room, sensors):
    # Функция для определения того, находится ли точка в радиусе действия сенсора
    def is_covered_by_sensors(x, y):
        for i in range(len(sensors)):
            # Сравниваем расстояние от точки до центра сенсора и радиус сенсора
            if (x - sensors[i][0]) ** 2 + (y - sensors[i][1]) ** 2 <= sensors[i][2] ** 2:
                return True
        return False
    # Проверяем каждую точку комнаты
    x = 0
    y = 0
    while x <= (room[0]):
        while y <= (room[1]):
            if not is_covered_by_sensors(x, y):
                return False
            else:
                y += 0.001
        x += 0.001
    return True 


room = [4,6]
sensors = [[1,1,1], [3, 3, 3]]


plt.axis([0, room[0], 0, room[1]]) 
plt.axis('square')


for j in range(len(sensors)):
    c = plt.Circle((sensors[j][0], sensors[j][1]), radius= sensors[j][2] ) #generating circle
    plt.gca().add_artist(c) # adding circle to plot
print(is_covered(room, sensors))