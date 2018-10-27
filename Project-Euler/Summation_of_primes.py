import math

num = 1
total = 1 
limit = 2000000

def prime_check(num):
    n = math.ceil(math.sqrt(num))
    i = 2

    while i <= n:

        if num % i == 0:    
            return False
    
        i += 1
        
    return True

while num < limit:

    