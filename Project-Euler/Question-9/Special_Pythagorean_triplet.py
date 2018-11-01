import math
import time 

'''
a = 1
b = 0
c = 0
d = 1 
s = 1000
f = s/3
found = False
'''

#vars#
i = 1000
a =1
b =1
c =1

start = time.time()
def pythagorean(a ,b):
    c = math.sqrt(((a ** 2) + (b ** 2))) 
    if c % 1 == 0:
        return True
    else:
        return False

def pythagorean_triple(a,b,c):
        if c**2 == ((a ** 2) + (b ** 2)):
                return True
        else:
                return False
'''
for d in range(1,f,1):
    e = s - d 
    #print (d,e)

    g = pythagorean(d,e)

    if g:
        
        break
    else:
        print(d,e)
'''
'''
a = 1
b = 1


while a <= 1000//3:
        b = 1 
        while b<=1000//2:
                if pythagorean(a,b):
                        break 
                        
                else:
                        b+=1 
                        print(a,b)
        if pythagorean(a,b) and a + b + math.sqrt(((a ** 2) + (b ** 2))) == 1000:
                break
        else:
                a+=1
'''


#find where a+b+c = 1000 then check pythagorean

for a in range(1,(i//3),1):
        for b in range (1,(i//2),1):
                c = i-(a+b)
                
                if a + b + c == i and pythagorean_triple(a,b,c):
                        break
        if a + b + c == i and pythagorean_triple(a,b,c):
                break
        
                        
d = a*b*c
elapsed = time.time() - start
print(a,b,c,d,elapsed)