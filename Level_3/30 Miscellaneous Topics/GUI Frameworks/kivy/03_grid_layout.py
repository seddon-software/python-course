import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.title = 'Grid Layout'
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=400)
        layout.add_widget(Button(text='Button 1-1', size_hint_x=None, width=150))
        layout.add_widget(Button(text='Button 1-2'))
        layout.add_widget(Button(text='Button 2-1', size_hint_x=None, width=150))
        layout.add_widget(Button(text='Button 2-2'))
        return layout

MyApp().run()
