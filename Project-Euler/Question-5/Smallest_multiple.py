#find smallest multiple that the numbers 1-20 deivied evenly into 
#had to stop at 80427044 (needed to use the computer)
import time

num = 1
def check(num):
    if num % 1 == 0 and num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0:
        return True 
    else:
        return False

start = time.time() 

while check(num) != True:
    print(num)
    num += 1
    check(num)

elapsed = time.time() - start

print(num, elapsed)