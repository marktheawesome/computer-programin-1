#find smallest multiple that the numbers 1-20 deivied evenly into 
#had to stop at 80427044 (needed to use the computer)
import time
'''
20 = 2^2 * 5 
19 = 19 
18 = 2 * 3^2 
17 = 17 
16 = 2^4 
15 = 3 * 5 
14 = 2 * 7 
13 = 13 
11 = 11 

'''
num = 1
def check(num):
    if  num % 11 == 0 and  num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0:
        return True 
    else:
        return False

start = time.time() 

while check(num) != True:
    print(num)
    num += 2
    check(num)

elapsed = time.time() - start

print(num, elapsed)