from kivy.uix.button import Button 
from kivy.app import App
from functools import partial
 
class KivyButton(App):
 
    def disable(self, instance, *args):
        instance.disabled = True
 
    def update(self, instance, *args):
        instance.text = "I am Disabled!"
 
    def build(self):
        self.title = 'Binding functions'
        b = Button(text="Hit me!", 
                   pos=(300,350), 
                   size_hint = (.25, .18))
 
        b.bind(on_press=partial(self.disable, b))
        b.bind(on_press=partial(self.update, b))
 
        return b
 
KivyButton().run()
