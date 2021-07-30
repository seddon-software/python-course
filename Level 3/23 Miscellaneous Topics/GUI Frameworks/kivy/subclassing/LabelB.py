from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<LabelB>:
  pos_hint: 1.0, 1.0
  size_hint: .8, .8
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class LabelB(Label):
  #bcolor = ListProperty([1,1,1,1])
  pass
Factory.register('MyLabelB', module='LabelB')
