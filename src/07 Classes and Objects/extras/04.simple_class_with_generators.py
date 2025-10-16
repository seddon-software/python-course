'''
This example shows how to use a coroutine to implement the functionality of a class.  As you 
can see it is somewhat ugly, but works because a coroutine maintains state..
'''

def Point(x0, y0, name):
    self = {}
    self['name'] = name
    self['x'] = x0
    self['y'] = y0
    while True:
        cmd = yield
        match cmd[0]:
            case 'moveBy':
                self['x'] += cmd[1]
                self['y'] += cmd[2]
                yield None
            case 'display':
                yield f"{self['name']} is at [{self['x']}, {self['y']}]"

def main():
    p1 = Point(100, 200, "point-p1")
    p2 = Point(110, 230, "point-p2")
    p3 = Point(150, 270, "point-p3")
    next(p1)
    next(p2)
    next(p3)
    p1.send(('moveBy', 10, 20))
    p2.send(('moveBy', 11, 21))
    p3.send(('moveBy', 12, 22))
    next(p1)
    next(p2)
    next(p3)
    print( p1.send(('display',)) )
    print( p2.send(('display',)) )
    print( p3.send(('display',)) )

main()
