# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1129,770 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"问题" ), wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"题干", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		sbSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		sbSizer3.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText2 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"请输入答案", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		sbSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		sbSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"提交我的答案", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"进入下一道题", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( fgSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"判定结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl3.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer2.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"查看正确答案", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl4.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer2.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"开始测验", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl2.Bind( wx.EVT_TEXT, self.clearJudgement )
		self.m_button1.Bind( wx.EVT_BUTTON, self.submitAnswer )
		self.m_button2.Bind( wx.EVT_BUTTON, self.goNextQuestion )
		self.m_button3.Bind( wx.EVT_BUTTON, self.displayAnswer )
		self.m_button4.Bind( wx.EVT_BUTTON, self.startTest )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def clearJudgement( self, event ):
		event.Skip()
	
	def submitAnswer( self, event ):
		event.Skip()
	
	def goNextQuestion( self, event ):
		event.Skip()
	
	def displayAnswer( self, event ):
		event.Skip()
	
	def startTest( self, event ):
		event.Skip()
	

