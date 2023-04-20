sum = 0
def fact(x):
    if (x > 1):
        return x * fact(x-1)
    elif (x == 1 or x == 0):
        return 1
for i in range(5):
    f = fact(i)
    sum += 1/f
print(sum)