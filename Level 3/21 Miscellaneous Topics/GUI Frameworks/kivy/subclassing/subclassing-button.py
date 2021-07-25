import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, Line

from kivy.app import App
from kivy.lang import Builder

from LabelB import LabelB
from LabelC import LabelC
from LabelD import LabelD

# Builder.load_string("""
# <MyGrid>:
#   rows: 3
#   LabelD:
#     bcolor: 1,0,0,1
#   LabelB:
#     bcolor: 0,1,0,1
#   LabelD:
#     bcolor: 0,1,1,1
# """)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        self.size_hint = (0.9, 0.9)
        super(GridLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0, 0, 1)
            
class TheApp(App):
    def build(self):
        self.title = "Subclassing Button"
        Builder.load_file('widgetst.kv')
        grid = MyGrid(rows=3)
#         d1 = LabelD()
#         d1.bcolor = (1,0,0,1)

        b  = LabelB()
#        b.bcolor = (0,1,1,1)
        grid.add_widget(b)

        b  = LabelB()
#        b.bcolor = (1,1,0,1)
        grid.add_widget(b)
        
        d  = LabelD()
#        d.bcolor = (1,0,1,1)
        grid.add_widget(d)

        return grid

TheApp().run()
