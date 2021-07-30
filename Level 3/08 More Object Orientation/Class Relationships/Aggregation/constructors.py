class Computer:
    def __init__(self, n, r, d, p, s, rx, ry):
        screen = Screen(s, rx, ry)
        self.name = n
        self.ram = r
        self.disk = d
        self.processor = p
        self.screen = screen

class Screen:
    def __init__(self, s, rx, ry):
        r = Resolution(rx, ry)
        self.size = s
        self.resolution = r

class Resolution:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
dell = Computer("Vostro", "2GB", "160GB", "Intel", 24, 1440, 900)
toshiba = Computer("Satellite", "3GB", "140GB", "AMD", 24, 1920, 1200)

