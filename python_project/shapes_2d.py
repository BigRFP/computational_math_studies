import math

def square(s):
    perimeter = 4*s
    area = s*s
    return perimeter,area

def rectangle(l,w):
    perimeter = 2*l+2*w
    area = l*w
    return perimeter,area

def circle(r):
    d = r*2
    perimeter = math.pi*d
    area = math.pi*r**2
    return d,perimeter,area