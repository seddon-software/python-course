############################################################
#
#    menus
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
    
    def AddMenu(self):
        self.menubar = wx.MenuBar()

        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()
        
        file.Append(text = '&Open', help = 'Open a new document', id = MyFrame.ID_OPEN)
        file.Append(text = '&Save', help = 'Save the document', id = MyFrame.ID_SAVE)
        file.AppendSeparator()
        file.Append(text = 'E&xit', help = 'Exit', id = MyFrame.ID_EXIT)
        
        self.menubar.Append(file, '&File')
        self.menubar.Append(edit, '&Edit')
        self.menubar.Append(help, '&Help')
        self.SetMenuBar(self.menubar)

    

app = MyApp()
app.MainLoop()

