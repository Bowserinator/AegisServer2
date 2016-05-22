import math

    
def distance2D(x1,y1,x2,y2):
    a = x2 - x1
    b = y2 - y1
    return math.sqrt(a*a + b*b)
    
def distance3D(x1,y1,z1,x2,y2,z2):
    a = x2 - x1
    b = y2 - y1
    c = z2 - z1
    return math.sqrt(a*a + b*b + c*c)
    
def chunkToCoordinates(x,z):
    return [x*16, z*16]
    
def coordinatesToChunk(x,z):
    return [math.floor(x/16.0),math.floor(z/16.0)]


