import math
import time 
start = time.time() 
num = 1
limit = 10001
prime_id = 0

def prime_check(num):
    n = math.ceil(math.sqrt(num))
    i = 2

    while i <= n:

        if num % i == 0:    
            return False
    
        i += 1
        
    return True

while prime_id < limit:
    is_prime = prime_check(num)
    if is_prime:
        if limit > prime_id:
            #print(num)
            prime_id += 1
            num += 2
        else:
            pass
    else:
        num+=2
    #print(num)
num = num -2
elapsed = time.time() - start
print (num,elapsed)
