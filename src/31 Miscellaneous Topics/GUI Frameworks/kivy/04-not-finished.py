from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from functools import partial

Builder.load_string("""
<MyBoxLayout>:
    Button:
        size_hint: 0.2, 0.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        background_normal: ''
        background_color: 0, 1, 0, .5
        text: "My Button"
        orientation: 'horizontal'
        canvas.after:
            Color:
                rgba: 1, 0, 0, 1
            Line:
                width: 20
                rectangle: self.center_x-self.width/2, self.center_y-self.height/2, self.width, self.height
        border: (10,10,10,10)
        Image:
            pos_hint:{'x':0, 'y':0}
            size: (400, 400)
            background_color: 0, 1, 1, .85
            source: 'images.jpg'
            center_x: self.parent.center_x
            center_y: self.parent.center_y
""")

class MyBoxLayout(App, BoxLayout):
    
    def build(self):
        def my_callback(box, t):
            self.parent.clearcolor = (0.2, 0.3, 0.7, 1)
            print(f"center={box.center}")
            print(f"height={box.height}")
            print(f"width={box.width}")
            print(f"orientation={box.orientation}")
        self.size_hint = (0.8, 0.8)
        self.pos_hint = {'center_x':0.5, 'center_y':0.5}
        self.title = "Using a .kv string"
        Window.size = (800, 500)
        Clock.schedule_once(partial(my_callback, self), -1)

        return self
    
MyBoxLayout().run()
