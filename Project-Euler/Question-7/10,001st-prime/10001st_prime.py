import math
import time 
start = time.time() 
num = 1
limit = 10001
prime_id = 0

def prime_check(num):
    n = num - 1

    while n > 1:

        if num % n == 0 and n >= 1 :
            return False

        n = n-1 

    return True

while prime_id < limit:
    is_prime = prime_check(num)
    if is_prime:
        if limit > prime_id:
            print(num)
            prime_id += 1
            num += 2
        else:
            break
    else:
        num+=2
    print(num)
num = num -2
elapsed = time.time() - start
print (num,elapsed)

# Wrong (104731, 263.098680973053) @ limit 10,000
#105753
# WTF (104745, 249.62721991539001) @ limit 10,001
#(104761, 339.1306540966034)