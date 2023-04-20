import math
sum = 0
k = 1
while True:
    sum += (-1)**(k+1)/(k**2)
    if abs(sum - math.pi**2/12) <= 10**(-10):
        print(k)
        break
    k += 1