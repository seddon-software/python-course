class Computer:
    def __init__(self, n, r, d, p, s, rx, ry):
        screen = Screen(s, rx, ry)
        self.name = n
        self.ram = r
        self.disk = d
        self.processor = p
        self.screen = screen
    
    def GetDetails(self):
        return "name=" + self.name + "\n" + \
               "ram=" + self.ram  + "\n" + \
               "disk=" + self.disk  + "\n" + \
               "processor=" + self.processor  + "\n" + \
               "screen: " + self.screen.GetDetails() + "\n";

class Screen:
    def __init__(self, s, rx, ry):
        r = Resolution(rx, ry)
        self.size = s
        self.resolution = r

    def GetDetails(self):
        return "size=" + str(self.size) + ", " + \
               "resolution: " + self.resolution.GetDetails()
        
class Resolution:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def GetDetails(self):
        return "x=" + str(self.x) + "," + \
               "y=" + str(self.y)

dell = Computer("Vostro", "2GB", "160GB", "Intel", 24, 1440, 900)
toshiba = Computer("Satellite", "3GB", "140GB", "AMD", 24, 1920, 1200)
print(dell.GetDetails())
print(toshiba.GetDetails())

1