############################################################
#
#    event handlers
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
        self.frame = MyFrame("Frame")
        self.frame.Show()
        return True;

class MyFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, parent = None, title = title, size = (200, 400))
        self.file = wx.Menu()
        self.edit = wx.Menu()
        self.help = wx.Menu()

        self.open = wx.MenuItem(self.file, next(idGenerator), "Open")
        self.save = wx.MenuItem(self.file, next(idGenerator), "Save")
        self.quit = wx.MenuItem(self.file, next(idGenerator), "Quit")
        self.exit = wx.MenuItem(self.file, next(idGenerator), "Exit")

        self.file.AppendItem(self.open)
        self.file.AppendItem(self.save)
        self.file.AppendSeparator()
        self.file.AppendItem(self.quit)
        self.file.AppendItem(self.exit)

        self.Bind(wx.EVT_MENU, self.onOpen, id=self.open.GetId())
        self.Bind(wx.EVT_MENU, self.onSave, id=self.save.GetId())
        self.Bind(wx.EVT_MENU, self.onQuit, id=self.quit.GetId())
        self.Bind(wx.EVT_MENU, self.onExit, id=self.exit.GetId())
                
        self.menubar = wx.MenuBar()
        self.SetMenuBar(self.menubar)

        self.menubar.Append(self.file, '&File')
        self.menubar.Append(self.edit, '&Edit')
        self.menubar.Append(self.help, '&Help')
        
    def popUp(self, message):
        dlg = wx.MessageDialog(self, message, "Event", wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
    def onOpen(self, event): self.popUp("Open selected")
    def onSave(self, event): self.popUp("Save selected")
    def onQuit(self, event): self.popUp("Quit selected")
    def onExit(self, event): self.Close(True)
        
        
app = MyApp()
app.MainLoop()

