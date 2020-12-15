import math

class Vec3(object):
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        if type(x) not in [float, int] \
            and type(y) not in [float, int] \
                and type(z) not in [float, int]:
            raise TypeError("x, y, and z must be float or int")
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __eq__(self, rhs:'Vec3'):
        return self.x == rhs.x and \
            self.y == rhs.y and \
                self.z == rhs.z
    
    def __add__(self, rhs:'Vec3'):
        if not isinstance(rhs, Vec3):
            raise TypeError("rhs must be Vec3")
        return Vec3(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)

    def __pos__(self):
        return Vec3(self.x, self.y, self.z)
    
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __sub__(self, rhs:'Vec3'):
        return self.__add__(-rhs)

    def __mul__(self, rhs:float):
        if type(rhs) not in [float, int]:
            raise TypeError("rhs must be float or int")
        return Vec3(self.x * rhs, self.y * rhs, self.z * rhs)
    
    def __rmul__(self, lhs:float):
        if type(lhs) not in [float, int]:
            raise TypeError("lhs must be float or int")
        return self.__mul__(lhs)

    def __truediv__(self, rhs:float):
        if type(rhs) not in [float, int]:
            raise TypeError("rhs must be float or int")
        if rhs == 0.0:
            raise ValueError(f"rhs={rhs}, DIVISION BY ZERO")
        return Vec3(self.x/rhs, self.y/rhs, self.z/rhs)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def dot(self, rhs:'Vec3'):
        if not isinstance(rhs, Vec3):
            raise TypeError("rhs must be Vec3")
        return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z
    
    def cross(self, rhs:'Vec3'):
        if not isinstance(rhs, Vec3):
            raise TypeError("rhs must be Vec3")
        return Vec3(self.y * rhs.z - self.z * rhs.y,
                    -(self.x * rhs.z - self.z * rhs.x),
                    self.x * rhs.y - self.y * rhs.x)

def dot(lhs, rhs):
    if not (isinstance(lhs, Vec3) and isinstance(rhs, Vec3)):
        raise TypeError("lhs and rhs must be Vec3")
    return lhs.dot(rhs)

def cross(lhs, rhs):
    if not (isinstance(lhs, Vec3) and isinstance(rhs, Vec3)):
        raise TypeError("lhs and rhs must be Vec3")
    return lhs.cross(rhs)

def norm2(v):
    return math.sqrt(v.x*v.x + v.y*v.y + v.z*v.z)