import math
import time 

start = time.time() 

num = 1
total = 0 
limit = 2000000

def prime_check(num):
    n = math.ceil(math.sqrt(num))
    i = 2

    while i <= n:

        if num % i == 0:    
            return 0 
    
        i += 1
        
    return num 

#for num in range(0,limit,2):
while num <= limit:
    X1 =  prime_check(num)
    total = total + X1
    num +=2


elapsed = time.time() - start

print(total+1, elapsed)