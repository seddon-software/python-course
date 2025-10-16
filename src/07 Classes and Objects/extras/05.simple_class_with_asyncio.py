'''
This example shows how to use an async coroutine to implement the functionality of a class.  
This is still pretty ugly, but shows what can be done.

Note the use of 'anext' and 'asend' in place of 'next' and 'send' (Python 3.10+)
'''

import asyncio


async def Point(x0, y0, name):
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
                await asyncio.sleep(0)
            case 'display':
                yield f"{self['name']} is at [{self['x']}, {self['y']}]"
                await asyncio.sleep(0)

async def main():
    p1 = Point(100, 200, "point-p1")
    p2 = Point(110, 230, "point-p2")
    p3 = Point(150, 270, "point-p3")
    await anext(p1)
    await anext(p2)
    await anext(p3)
    await p1.asend(('moveBy', 10, 20))
    await p2.asend(('moveBy', 11, 21))
    await p3.asend(('moveBy', 12, 22))
    await anext(p1)
    await anext(p2)
    await anext(p3)
    print( await p1.asend(('display',)) )
    print( await p2.asend(('display',)) )
    print( await p3.asend(('display',)) )

asyncio.run(main())
