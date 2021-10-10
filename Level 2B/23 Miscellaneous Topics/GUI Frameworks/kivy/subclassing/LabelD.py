from kivy.uix.label import Label
from kivy.properties import ListProperty, ObservableList
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Line

# Builder.load_string(f"""
# <LabelX>:
#   bcolor: 1, 1, 1, 1
#   canvas.before:
#     Color:
#       rgba: 1, 0, 0, 1
#     Rectangle:
#       pos: self.pos 
#       size: self.size
#   canvas:
#     Color:
#       rgba: self.bcolor
#     Rectangle:
#       pos: [self.size[0]*0.02, self.size[1]*0.02] 
#       size: [x*.96 for x in self.size]
# """)

# height: self.width / 2. if self.disabled else self.width
# ...     x: self.y + 50

class LabelD(Label):
    bcolor = ListProperty([1,1,1,1])
    def __init__(self, **kwargs):
        #self.size_hint = (0.5, 0.5)
        self.size = (200, 200)
        super(Label, self).__init__(**kwargs)
        print(f"{self.__class__.__name__} pos:{self.pos} size: {self.size}")
#        self.size_hint = (2, 2)
        with self.canvas.before:
            Color(1, 0, 0, 1)
            # Line(width = 200)
            Rectangle(
                pos=(400,200),
#                    pos_hint={'center_x': .5, 'center_y': .5}, 
                      size_hint={'x':500, 'y':50},
#                      size=(300,300)
                      )
        with self.canvas.after:
            Color(1, 1, 0, 1)
            # Line(width = 200)
            Rectangle(pos_hint={'center_x': .5, 'center_y': .5}, 
                      size_hint={'x':1, 'y':1})
            print(f"{self.__class__.__name__} pos:{self.pos} size: {self.size}")
Factory.register('MyLabelD', module='LabelD')
