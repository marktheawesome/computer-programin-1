import math
import time 
a = 1
b = 0
c = 0
s = 1000
found = False

start = time.time()

def Pythagorean(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

a = [x for x in range(1,1000)]

for num in a:
    for dig in range (num, 1000 - num):
        for i in range(dig, 1000 - dig):
            if num + dig + i == 1000:
                if Pythagorean(num, dig, i):
                    print(num, dig, i)
                    print("Product: {}".format(num * dig * i))
                    elapsed = time.time() - start
                    print("Time: {:.5f} seconds".format(elapsed))
                    exit(1)
