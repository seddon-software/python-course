#!/usr/bin/env python

import wx, time

# Create the custom event.
myEVT_CUSTOM_EVENT = wx.NewEventType()
EVT_CUSTOM_EVENT = wx.PyEventBinder(myEVT_CUSTOM_EVENT, 1)

class MyEvent(wx.PyEvent):
    def __init__(self, event_type, id):
        wx.PyEvent.__init__(self, id, event_type)
        # Note that the id and event_type are reversed 
        # from wx.PyCommandEvent
        self.myVal = "didn't fire properly."

    def setMyVal(self, val):
        self.myVal = val

    def getMyText(self):
        return self.myVal   

class MyProcess(object):
    # Process that creates events as it works
    def __init__(self, myWidget):
        self.myWidget = myWidget

    def process_data(self):
        for i in range(6):
            print "Outputting number %s" % i
            self.update_gui(i)
            time.sleep(.75)

    def update_gui(self, val):
        #create a custom event object and enter it in the event queue:
        evt = MyEvent(myEVT_CUSTOM_EVENT, self.myWidget.GetId() )
        evt.setMyVal(val)
        self.myWidget.GetEventHandler().ProcessEvent(evt)

class MyGUI(object):
    def __init__(self):
        frame = wx.Frame(None, -1, "Custom Events")
        panel = wx.Panel(frame, -1)
        button = wx.Button(panel, -1, "Start", pos=(100, 10))
        button.Bind(wx.EVT_BUTTON, self.onclick)
        self.text_ctrl = wx.TextCtrl(panel, -1, "Ready...\n",
            pos=(50, 50), size=(300, 120), style=wx.TE_MULTILINE)
        self.a = MyProcess(self.text_ctrl)
        self.text_ctrl.Bind(EVT_CUSTOM_EVENT, self.on_my_event, id=self.text_ctrl.GetId())
        frame.Show()

    def onclick(self, event):
        self.a.process_data()

    def on_my_event(self, event):
        self.text_ctrl.AppendText("Event %s\n" % (event.getMyText(), ))

if __name__ == '__main__':
    app = wx.PySimpleApp(redirect=False)
    MyGUI()
    app.MainLoop()
