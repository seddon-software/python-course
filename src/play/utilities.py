import numpy as np

#np.set_printoptions(precision=2)
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

def step(x, charge, width, dx):
    '''
    x = distance from particle
    charge = normal value
    width = width of step
    dx = granularity of function
    
    returns y = field value (unnormalised)
    '''
    distance = x.mod()
    gap = int(1/dx)
    width = int(width/dx)
    print(f"debug: {distance}, {int(distance/dx)}")
    r = range(-width, width+1)  # range of values where force is flipped
    if int((distance / dx)) % gap in r:
        return -charge / distance**2
    else:
        return charge / distance**2

class V:
    def __init__(self, vx0, vy0, vz0):
        self.velocity = np.array([vx0, vy0, vz0]).astype('float')
    def __str__(self):
        return f"{self.velocity[0:3]}"
    
    def __iter__(self): 
        return iter(self.velocity.tolist())

class S:
    def __init__(self, x0, y0, z0):
        self.position = np.array([x0, y0, z0]).astype('float')

    def __str__(self):
        return f"{self.position[0:3]}"
    
    def __iter__(self): 
        return iter(self.position.tolist())
    
    def mod(self):
        return np.dot(self.position, self.position) ** 0.5


class Particle:
    def __init__(self, s, v):
        self.position = S(*s)
        self.velocity = V(*v)

    def __str__(self):
        return f"s={self.position}, v={self.velocity}"

class Electron(Particle):
    def __init__(self, s, v):
        Particle.__init__(self, s, v)
    def force(self, s):
        return step(s, -1, 0.03, 0.01)
    
if __name__ == '__main__':
    v1 = V(3.7, 4, 5)
    s1 = S(2, 4, 6)
    s2 = S(3., 0.4, 0)
    print(v1)
    print(s1)
    print(s2.mod())
    p = Electron(s1, v1)
    print(p)
    print(p.force(s2))

        