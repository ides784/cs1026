import math
# defining the three functions containing formulas for the shapes
def cubevol(a):
    return (a*a*a)

def pyramidvol(b, h):
    return ((1/3)*(b*b)*h)

def ellipsoidvol(r1, r2, r3):
    return ((4/3)*(math.pi)*r1*r2*r3)
