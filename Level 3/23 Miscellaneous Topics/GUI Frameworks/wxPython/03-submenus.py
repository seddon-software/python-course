############################################################
#
#    submenus
#
############################################################

import wx


class MyApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame("Hello")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True;


class MyFrame(wx.Frame):

    ID_OPEN = 100
    ID_SAVE = 101
    ID_EXIT = 102

    def __init__(self, title):
         wx.Frame.__init__(self, 
                           parent = None, 
                           title = title,
                           pos = (100, 300),
                           size = (200, 400))
         self.AddMenu()
         self.AddSubMenu()


    def AddMenu(self):
        self.menubar = wx.MenuBar()

        self.file = wx.Menu()
        self.edit = wx.Menu()
        self.help = wx.Menu()
        
        self.file.Append(text = '&Open', help = 'Open a new document', id = MyFrame.ID_OPEN)
        self.file.Append(text = '&Save', help = 'Save the document', id = MyFrame.ID_SAVE)
        self.file.AppendSeparator()
        self.file.Append(text = 'E&xit', help = 'Exit', id = MyFrame.ID_EXIT)
        
        self.menubar.Append(self.file, '&File')
        self.menubar.Append(self.edit, '&Edit')
        self.menubar.Append(self.help, '&Help')
        self.SetMenuBar(self.menubar)

    def AddSubMenu(self):
        self.submenu = wx.Menu()
        self.submenu.Append(text = 'item1', kind=wx.ITEM_RADIO, id = wx.ID_ANY)
        self.submenu.Append(text = 'item2', kind=wx.ITEM_RADIO, id = wx.ID_ANY)
        self.submenu.Append(text = 'item3', kind=wx.ITEM_RADIO, id = wx.ID_ANY)
        self.file.AppendMenu(text = 'submenu', submenu = self.submenu, id = wx.ID_ANY)

app = MyApp()
app.MainLoop()
