import math
kat1 = 4
alpha = 60
gip = kat1 / math.sin(alpha) 
kat2 = math.sqrt(gip**2-kat1**2)
s = 0.5 * kat1 * kat2
print (s)