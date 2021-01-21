class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"__str__: {self.x, self.y, self.z}"

    def __repr__(self):
        return f"__repr__:{self.x, self.y, self.z}"

    def __format__(self, format_spec: str):
        if not format_spec or format_spec == "s":
            return str(self)
        
        if format_spec == "r":
            return f"r:{self.x, self.y, self.z}"
        if format_spec == "w":
            return f"w:{self.x, self.y, self.z}"
p = Point(1, 2, 3)
print(f"{p!s}")
print(f"{p!r}")
print(f"{p:s}")
print(f"{p:r}")
print(f"{p:w}")


