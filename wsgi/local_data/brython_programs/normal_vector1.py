import math
class Coord(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self,other):
        # This allows you to substract vectors
        return Coord(self.x-other.x,self.y-other.y)

    def __repr__(self):
        # Used to get human readable coordinates when printing
        return "Coord(%f,%f)"%(self.x,self.y)

    def length(self):
        # Returns the length of the vector
        return math.sqrt(self.x**2 + self.y**2)

    def angle(self):
        # Returns the vector's angle
        return math.atan2(self.y,self.x)

def normalize(coord):
    return Coord(
        coord.x/coord.length(),
        coord.y/coord.length()
        )

def perpendicular(coord):
    # Shifts the angle by pi/2 and calculate the coordinates
    # using the original vector length
    return Coord(
        coord.length()*math.cos(coord.angle()+math.pi/2),
        coord.length()*math.sin(coord.angle()+math.pi/2)
        )

a = Coord(2,12)
b = Coord(7,5)
print(perpendicular(normalize(a-b)).x, perpendicular(normalize(a-b)).y)