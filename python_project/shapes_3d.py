import math

def cube(r):
    surfaceArea = 6*(r*r)
    volume = r ** 3
    return surfaceArea,volume

def cuboid(l,w,h):
    surfaceArea = 2*((l*w)+(l*h)+(w*h))
    volume = l*w*h
    return surfaceArea,volume

def sphere(r):
    d = r*2
    surfaceArea = 4*math.pi*r**2
    volume = 4/3*math.pi*r**3
    return d,surfaceArea,volume