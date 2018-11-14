#find the lagest palindrome numuber from product of 2 three digit numbers
# 99 < n < 1000
import time 
start = time.time()

a = 100
b = 100
current_high = 0
num = a*b


def palindrome(num,current_high):
    if str(num) == str(num)[::-1] and num > current_high:
        return num
    
    return current_high 
        

while a < 1000 and b < 1000:
    current_high = palindrome(num,current_high)
    if a == 999:
        b = b + 1
        a = 100
    a = a+1
    
    num = a*b

elapsed = time.time() - start
print (current_high,elapsed)