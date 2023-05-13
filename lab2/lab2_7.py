import numpy as np
import matplotlib.pyplot as plt

funcDots = [(1, 1), (2, 5), (3, 4), (4, 10), (5, 11)]

def MainFunc(dots, num, lenSum):
    if num < len(dots)-1:
        lenSum += np.sqrt((dots[num+1][0] - dots[num][0])**2 + (dots[num+1][1] - dots[num][1])**2)
        return MainFunc(dots, num+1, lenSum)
    else:
        return lenSum

print(MainFunc(funcDots, 0, 0))

x, y = zip(*funcDots)
plt.plot(x, y)
plt.show() # upd