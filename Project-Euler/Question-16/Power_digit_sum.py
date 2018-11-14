'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
num = 2**1000
num = str(num)
total = 0
loc= 0 
for loc in range(0,len(num)):
    n = num[loc]
    n = int(n)
    total = n + total 
    print(loc)
total = str(total)
print(len(num),total)