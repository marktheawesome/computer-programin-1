# Mark Gyomory
#August 22,2018

'''
v is volume 
a is area 
'''

import math

pi = math.pi
e = math.e
sqrt = math.sqrt

print(pi)

print(e)

print(math.sqrt(2))

print(math.sin(0.5))


def triangle_area(b,h):
    a = (b*h)/2
    return a

def circle_area(r):
    a = pi * r**2
    return a

def trapezoid_area (a,b,h):
    a = ((a+b)/2)/h
    return a

def parallelogram_area(b,h):
    a = b * h
    return a

def rectangular_prism_volume(w,h,l):
    v = w * h * l
    return v

def cone_volume(r,h):
    v = pi * r ** 2 * (h/3)
    return v
    
def sphere_volume(r):
    v = (4/3) * pi * r ** 3 
    return v

def rectangular_prism_surface_area(w,h,l):
    sa = 2 * ( w * l + h * l + h * w) 
    return sa

def sphere_surface_area(r):
    sa = 4 * pi * r ** 2 
    return sa

def hypotenus_of_right_triangle_given_two_legs(a,b):
    c = sqrt((a**2)+(b**2)) 
    return c

def heron_formula(a,b,c):
    s = (a + b + c) / 2
    area = ((s * (s - a) * (s - b) * (s - c)))**0.5
    return area

print( heron_formula(3,5,7))
print( heron_formula(5,10,15))
#print(heron_formula(3,8,12))

'''
Q: are you really smart?
    yes
Q: What happens when you try to get the area of a triangle with sides of 5,10, and 15?
    It out puts the area of the triangle 
Q: 3,8, and 12? Why?
    It gives an error. It happens because that triangle can not exists.
'''

print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(trapezoid_area(1,2,3))
print(parallelogram_area(1,2))
print(rectangular_prism_volume(1,2,3))
print(cone_volume(1,2))
print(sphere_volume(1))
print(rectangular_prism_surface_area(1,2,3))
print(sphere_surface_area(1))
print(hypotenus_of_right_triangle_given_two_legs(1,2))