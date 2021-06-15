#!/usr/bin/env python

import serial
import wx
from time import sleep

class LabKit_Serial():
    ser = serial.Serial()

class BlinkSlider(wx.Frame):

    def __init__(self, *args, **kw): ### Constructor
        LabKit_Serial.ser.baudrate = 2000000
        LabKit_Serial.ser.port = 'com3'
        LabKit_Serial.ser.open()

        super(BlinkSlider, self).__init__(*args, **kw)

        self.InitUI()
    
    def __del__(self): ### Destructor
        LabKit_Serial.ser.close()

    def InitUI(self):

        pnl = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        sld = wx.Slider(pnl, value=200, minValue=1, maxValue=5,
                        style=wx.SL_HORIZONTAL)

        sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        sizer.Add(sld, pos=(0, 0), flag=wx.ALL|wx.EXPAND, border=25)

        self.txt = wx.StaticText(pnl, label='200')
        sizer.Add(self.txt, pos=(0, 1), flag=wx.TOP|wx.RIGHT, border=25)

        sizer.AddGrowableCol(0)
        pnl.SetSizer(sizer)

        self.SetTitle('wx.Slider')
        self.Centre()

    def OnSliderScroll(self, e):

        obj = e.GetEventObject()
        val = obj.GetValue()

        blink_txt = 'led blink' + " " + str(val)
        blink = 'blink_txt\r\n'
        LabKit_Serial.ser.write(blink_txt.encode('utf-8'))
        print(blink_txt)

        self.txt.SetLabel(str(val))

def main():

    app = wx.App()
    ex = BlinkSlider(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()  