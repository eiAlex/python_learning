# -*- coding: utf-8 -*-

from wx import  *

ID_ABOUT = 101
ID_EXIT = 102

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(200, 150))
        self.CreateStatusBar()
        self.SetStatusText("Este e a barra de Status")
        menu = wx.Menu()
        menu.Append(ID_ABOUT, "&Abount", "Mais informações sobre este programa")
        menu.AppendSeparator()
        menu.Append(ID_EXIT, "&Exit", "Finaliza o programa")
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "&File")
        self.setMenuBar(menuBar)

class MyAPP(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "HELLO FROM WX.PYTHON")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyAPP(0)
app.MainLoop()