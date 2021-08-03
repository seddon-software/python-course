############################################################
#
#    Minimal Program
#
############################################################

import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame("Hello")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

class MyFrame(wx.Frame):
    def __init__(self, title):
         wx.Frame.__init__(self, 
                           parent = None, 
                           title = title,
                           pos = (50, 100),
                           size = (200, 400))
    
app = MyApp()
app.MainLoop()
    