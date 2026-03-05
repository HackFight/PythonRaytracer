import math

class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    # Unary operators
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    
    #Binary operators
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return vec3(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other):
        return vec3(self.x / other, self.y / other, self.z / other)
    
    def __pow__(self, other):
        return vec3(self.x ** other, self.y ** other, self.z ** other)
    
    #Comparison operators
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __neq__(self, other):
        return not self.x != other.x or self.y != other.y or self.z != other.z
    
    #Custom operators
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return vec3(self.x * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def normalise(self):
        return self / self.magnitude()

class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

def HitSphere(r, center, radius):
    oc = center - r.origin
    a = r.direction.dot(r.direction)
    b = -2.0 * r.direction.dot(oc)
    c = oc.dot(oc) - radius**2
    discriminant = b**2 - 4*a*c
    return discriminant >= 0

if __name__ == "__main__":
    v = vec3(1, 1, 1)
    w = vec3(2, 0, 0)
    a = 5
    print(f"-{v} = {-v}")
    print(f"{v} + {w} = {v+w}")
    print(f"{v} - {w} = {v-w}")
    print(f"{v} * {a} = {v*a}")
    print(f"{v} / {a} = {v/a}")
    print(f"{v} ** {a} = {v**a}")
    print(f"{v} == {w} is {v==w}")
    print(f"{v} != {w} is {v!=w}")
    print(f"Magnitude of {v} is {v.magnitude()}")
    print(f"Dot product of {v} and {w} is {v.dot(w)}")
    print(f"Cross product of {v} and {w} is {v.cross(w)}")