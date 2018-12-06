import time 
start = time.time()
million = 4000000
total = 0 
a = 1
b = 1

while a+b <= million:
    c = a + b
    if c % 2 == 0:
        total = total + c 
    b,a = c,b

elapsed = time.time() - start
print (total,elapsed)