import numpy as np
import numpy.random as rand
import random
import math

print("Задание 1")
r1 = [1.18, 3.27]
int_list = random.sample(range(100, 1000), 98)
float_list = [x/100 for x in int_list]
r1 = r1 + float_list # upd
print(r1)
print("Задание 2")
r2 = rand.uniform(math.pi, math.pi * 10, (4, 25))
print(r2)
print("Задание 3")
r2 = r2.astype(np.int64) # upd
print(r2)
print("Задание 4")
ar100 = rand.randint(0, 100, 10)
indexes = random.sample(range(100), 10)
r3 = []
for i in indexes:
    r3.append(ar100[i])  # upd
print(r3)