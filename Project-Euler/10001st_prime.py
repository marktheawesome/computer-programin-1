import math
num = 1
limit = 10001
prime_id = 0

while prime_id < limit:
    if num % 2 == 0 or num % 3 ==0 or num % 5 == 0 or num % 7 == 0 :
        num +=1
    else:
        prime_id += 1
        num += 1 

print (num)