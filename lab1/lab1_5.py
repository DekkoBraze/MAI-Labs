import math
e = float(input())
if 1 < e < math.inf:
    print("Гиперболическая орбита")
elif 0 < e < 1:
    print("Эллиптическая орбита")
elif e == 0:
    print("Круговая орбита")
elif e == 1:
    print("Параболическая орбита")
elif e == math.inf:
    print("Прямая")
