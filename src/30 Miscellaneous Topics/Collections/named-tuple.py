import collections

# nametuple() is a factory method
Point = collections.namedtuple('Point', ['x', 'y', 'z', 'w'], verbose=False)

# now create instances of Point named tuple
p = Point(x = 100, y = 200, z = 300, w = 400)
q = Point(x = 111, y = 222, z = 333, w = 444)

# accessible by index or name
print(p[0], p[1], p[2], p[3])
print(p.x, p.y, p.z, p.w)

# print formatted representation of object
print(p)

# unpack like a regular tuple
a, b, c, d = p
print(a, b, c, d)

# replace fields
q = p._replace(y = 222, w = 444)
print(q)

# convert to dictionary
d = q._asdict()
print(d)

1
