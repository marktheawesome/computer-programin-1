import time 
start = time.time()
million = 4000000
total = 0 
a = 1
b = 1

# fibonacci sequence
# Fsub(n) = Fsub(n-1) + Fsub(n-2)
# c = a +b 
# c, b = b , a

while a+b <= million:
    c = a + b
    if c % 2 == 0:
        total = total + c 
    b,a = c,b

elapsed = time.time() - start
print (total,elapsed)