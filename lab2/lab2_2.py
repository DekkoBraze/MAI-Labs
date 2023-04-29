import numpy as np
import numpy.random as rand
import math

r1 = rand.uniform(0, 100, 100)
print("Задание 1")
for i in r1:
    print(i)
r2 = rand.uniform(math.pi, math.pi * 10, (4, 25))
print("Задание 2")
for i in r2:
    for j in i:
        print(j)
print("Задание 3")
for i in r2:
    for j in i:
        j = int(j)
        print(j)
print("Задание 4")
r3 = rand.randint(0, 100, 10)
for i in r3:
    print(i)