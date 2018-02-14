# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:21:15 2018

@author: actionfocus
"""

import wx
import demo

class CalcFrame(demo.MyFrame1):
    def __init__(self, parent):
        demo.MyFrame1.__init__(self, parent)
    
    def findsquare(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num*num))
        
app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
app.MainLoop()
