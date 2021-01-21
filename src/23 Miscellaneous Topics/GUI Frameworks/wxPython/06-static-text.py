############################################################
#
#    static text
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
                          pos = (50, 150),
                          size = (400, 400))
        try:
            self.AddMenu()
            self.AddSubMenu()
            self.SetupEventHandlers()
            self.AddButtons()
            self.AddStaticText()
        except Exception as e:
            print(e)

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

    def onOpen(self, event):
        dlg = wx.MessageDialog(self, "Open selected", "Event", wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    
    def onSave(self, event):
        dlg = wx.MessageDialog(self, "Save selected", "Event", wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def onExit(self, event):
        self.Close(True)

    def SetupEventHandlers(self):
        self.Connect(MyFrame.ID_OPEN, -1, wx.wxEVT_COMMAND_MENU_SELECTED, self.onOpen)
        self.Connect(MyFrame.ID_SAVE, -1, wx.wxEVT_COMMAND_MENU_SELECTED, self.onSave)
        self.Connect(MyFrame.ID_EXIT, -1, wx.wxEVT_COMMAND_MENU_SELECTED, self.onExit)
        
    ID_BUTTON1 = 103
    ID_BUTTON2 = 104
    ID_BUTTON3 = 105

    def onButton(self, event):
        buttonNo = event.Id - MyFrame.ID_BUTTON1 + 1
        message = "Button " + str(buttonNo) + " pressed"
        dlg = wx.MessageDialog(self, message, "Event", wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def AddButtons(self):
        self.panel = wx.Panel(self, -1)
        self.box = wx.BoxSizer(wx.HORIZONTAL)
        self.box.Add(wx.Button(self.panel, MyFrame.ID_BUTTON1, 'Button1'), 1 )
        self.box.Add(wx.Button(self.panel, MyFrame.ID_BUTTON2, 'Button2'), 1 )
        self.box.Add(wx.Button(self.panel, MyFrame.ID_BUTTON3, 'Button3'), 1 )
        self.panel.SetSizer(self.box)
        self.Bind(wx.EVT_BUTTON, self.onButton, id=MyFrame.ID_BUTTON1)
        self.Bind(wx.EVT_BUTTON, self.onButton, id=MyFrame.ID_BUTTON2)
        self.Bind(wx.EVT_BUTTON, self.onButton, id=MyFrame.ID_BUTTON3)

    def AddStaticText(self):
        textString1 = "The quick brown fox jumped over the lazy dog."
        textString2 = "To screw up is human\nbut to really screw up\nrequires a computer"        
        wx.StaticText(self.panel, -1, textString1, (45, 100), style=wx.ALIGN_CENTRE)
        wx.StaticText(self.panel, -1, textString2, (45, 190), style=wx.ALIGN_CENTRE)

        
app = MyApp()
app.MainLoop()

