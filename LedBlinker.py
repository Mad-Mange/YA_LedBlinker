#!/usr/bin/env python

import serial
import wx
from time import sleep

class LabKit_Serial():
    ser = serial.Serial()

class BlinkSlider(wx.Frame):

    def __init__(self, *args, **kw):
        LabKit_Serial.ser.baudrate = 2000000
        LabKit_Serial.ser.port = 'com3'
        LabKit_Serial.ser.open()

        LabKit_Serial.ser.write("led blink 1000\r\n".encode('utf-8'))

        super(BlinkSlider, self).__init__(*args, **kw)

        self.InitUI()
    
    def __del__(self):
        LabKit_Serial.ser.close()
        print("Running Destructor!!!!")

    def InitUI(self):

        pnl = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        sld = wx.Slider(pnl, value=1, minValue=1, maxValue=5,
                        style=wx.SL_HORIZONTAL)

        sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        sizer.Add(sld, pos=(0, 0), flag=wx.ALL|wx.EXPAND, border=25)

        self.txt = wx.StaticText(pnl, label='5')
        sizer.Add(self.txt, pos=(0, 1), flag=wx.TOP|wx.RIGHT, border=25)

        sizer.AddGrowableCol(0)
        pnl.SetSizer(sizer)

        self.SetTitle('wx.Slider')
        self.Centre()

    def OnSliderScroll(self, e):

        obj = e.GetEventObject()
        val = obj.GetValue()

        blink_txt = 'led blink' + " " + str(val * 1000) + '\r\n'
        LabKit_Serial.ser.write(blink_txt.encode('utf-8'))

        self.txt.SetLabel(str(val))

def main():

    app = wx.App()
    ex = BlinkSlider(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()  