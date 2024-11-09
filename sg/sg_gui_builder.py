# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"sg"), pos = wx.DefaultPosition, size = wx.Size( 731,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_waveformList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_waveformList.Enable( False )

        bSizer3.Add( self.m_waveformList, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_addCw = wx.Button( self, wx.ID_ANY, _(u"Add CW"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_addCw, 0, wx.ALL, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Frequency"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer6.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_cwFreq = wx.TextCtrl( self, wx.ID_ANY, _(u"0.1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_cwFreq, 0, wx.ALL, 5 )

        self.m_cwAmpl = wx.StaticText( self, wx.ID_ANY, _(u"Amplitude"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_cwAmpl.Wrap( -1 )

        bSizer6.Add( self.m_cwAmpl, 0, wx.ALL, 5 )

        self.m_cwAmpl = wx.TextCtrl( self, wx.ID_ANY, _(u"1.0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_cwAmpl, 0, wx.ALL, 5 )

        self.m_textCtrl6 = wx.StaticText( self, wx.ID_ANY, _(u"Initial Phase"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl6.Wrap( -1 )

        bSizer6.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

        self.m_cwInitPhase = wx.TextCtrl( self, wx.ID_ANY, _(u"0.0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_cwInitPhase, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_generate = wx.Button( self, wx.ID_ANY, _(u"Generate"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_generate, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Fs"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_fs = wx.TextCtrl( self, wx.ID_ANY, _(u"1.0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_fs, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"length"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_length = wx.TextCtrl( self, wx.ID_ANY, _(u"32"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_length, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_clearList = wx.Button( self, wx.ID_ANY, _(u"Clear List"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_clearList, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer9, 0, 0, 5 )


        bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnClose )
        self.m_addCw.Bind( wx.EVT_BUTTON, self.OnButtonClickAddCW )
        self.m_generate.Bind( wx.EVT_BUTTON, self.OnButtonClickGenerate )
        self.m_clearList.Bind( wx.EVT_BUTTON, self.OnButtonClickClearList )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnClose( self, event ):
        event.Skip()

    def OnButtonClickAddCW( self, event ):
        event.Skip()

    def OnButtonClickGenerate( self, event ):
        event.Skip()

    def OnButtonClickClearList( self, event ):
        event.Skip()


