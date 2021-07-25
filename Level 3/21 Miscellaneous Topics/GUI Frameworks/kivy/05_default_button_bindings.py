# switch off logging
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.uix.button import Button 
from kivy.app import App
from kivy.core.window import Window

class MyWidget(Button):
    '''
        THe button class already defines several Kivy properties:
        
        anchors                 : ObservableDict
        background_color        : ObservableList
        border                  : ObservableList
        center                  : ObservableReferenceList
        children                : ObservableList
        cls                     : ObservableList
        color                   : ObservableList
        disabled_color          : ObservableList
        disabled_outline_color  : ObservableList
        ellipsis_options        : ObservableDict
        ids                     : ObservableDict
        outline_color           : ObservableList
        padding                 : ObservableReferenceList
        pos                     : ObservableReferenceList
        refs                    : ObservableDict
        size                    : ObservableReferenceList
        size_hint               : ObservableReferenceList
        size_hint_max           : ObservableReferenceList
        size_hint_min           : ObservableReferenceList
        text_size               : ObservableList
        texture_size            : ObservableList
        
        If a Kivy property changes then the corresponding 'on_xxx' callback is invoked
        This uses the 'descriptor' protocol of Python and explains why they must be class level properties.
        You can also define your own class level properties, but these will need an explicit bind before a
            callback is invoked
        Most of the Button's Kivy properties will change when the button is first drawn, so the callbacks 
            will be invoked immediately.
        Examples of 'pos' and 'size' change callbacks are shown below:
    '''
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)
            
    def on_pos(self, button, pos):
        print(type(pos))
        print(f"window size = {Window.size}")
        print(f"object name = {button.name}")
        print(f"pos         = {pos}")
    
    def on_size(self, button, size):
        print(f"window size = {Window.size}")
        print(f"object name = {button.name}")
        print(f"size        = {size}")
        
    
class KivyButton(App):
    def build(self):
        self.title = 'Default Binding functions for Buttons'
        b = MyWidget(name='Button-1',
                     text="Hit me!", 
                     pos_hint={'x':0.5, 'y':0.5}, 
                     size_hint=(.25, .25))
        return b

KivyButton().run()
