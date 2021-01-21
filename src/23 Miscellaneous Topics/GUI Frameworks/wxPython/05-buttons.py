############################################################
#
#    buttons
#
############################################################

import wx

# generator for ids
def ids(): 
    for n in range(200, 1000): yield n
    return
idGenerator = ids()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame("Hello")
        self.frame.Show()
        return True;


class MyFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, parent = None, title = title, pos = (50, 150), size = (400, 400))
        self.AddButtons()

    def onButton(self, event):
        buttonNo = event.Id - self.button1.GetId() + 1
        message = "Button " + str(buttonNo) + " pressed"
        dlg = wx.MessageDialog(self, message, "Event", wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def AddButtons(self):
        self.panel = wx.Panel(self, -1)
        self.box = wx.BoxSizer(wx.HORIZONTAL)
        self.button1 = wx.Button(self.panel, next(idGenerator), 'Button1')
        self.button2 = wx.Button(self.panel, next(idGenerator), 'Button2')
        self.button3 = wx.Button(self.panel, next(idGenerator), 'Button3')
        self.box.Add(self.button1, 1 )
        self.box.Add(self.button2, 1 )
        self.box.Add(self.button3, 1 )
        self.panel.SetSizer(self.box)
        self.Bind(wx.EVT_BUTTON, self.onButton, self.button1)
        self.Bind(wx.EVT_BUTTON, self.onButton, self.button2)
        self.Bind(wx.EVT_BUTTON, self.onButton, self.button3)
        
app = MyApp()
app.MainLoop()

