import math 

x = math.factorial(100)
x = str(x)
total = 0

for i in range(len(x)):
    total += int(x[i])

print(total)
