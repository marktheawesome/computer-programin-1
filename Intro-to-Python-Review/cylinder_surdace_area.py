import math
pi = math.pi

def cylinder_surdace_area (r,h):
    a = (2 *pi * r * h + 2 * pi * r ** 2)
    return a

print ("radius")
r = input()
r = float(r)

print ("height")
h = input()
h = float(h)

print (cylinder_surdace_area(r,h))
