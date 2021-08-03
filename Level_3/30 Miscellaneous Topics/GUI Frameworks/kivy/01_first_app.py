from kivy.app import App
from kivy.uix.label import Label

class FirstKivy(App):
 
    def build(self):
        self.title = 'First Kivy App'
        return Label(text="Hello Kivy!")

FirstKivy().run()
