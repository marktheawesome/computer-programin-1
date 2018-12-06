import math
import time 

#vars#
i = 1000
a = 1
b = 1
c = 1

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
print(" "+str(a),"\n",b,"\n",c,"\n",d,"\n",elapsed)