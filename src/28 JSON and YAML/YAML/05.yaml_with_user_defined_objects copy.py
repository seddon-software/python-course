import yaml
from yaml.loader import UnsafeLoader

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        print("Point:", self.x, ":", self.y)

p = Point(5, 10)
yaml_obj = yaml.dump(p)

new_point = yaml.load(yaml_obj, Loader=UnsafeLoader)
print(new_point.x, new_point.y)
