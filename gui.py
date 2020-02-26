#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A MLHub GUI for AZCV

author: Graham Williams
website: mlhub.ai
"""

import os
import wx
import subprocess

MODEL = "Azure Computer Vision"

DEFAULT_PATH = "Enter a local path to an image (jpg, png) file"

WILDCARD = "Images (*.jpg,*.png)|*.jpg;*.png|" \
           "All files (*.*)|*.*"

class MLHub(wx.Frame):

    def __init__(self, parent, title):
        super(MLHub, self).__init__(parent,
                                    title=title,
                                    size=(750, 500))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        # self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.images_dir = os.path.join(os.getcwd(), "cache/images")
        
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc_path = wx.TextCtrl(panel, value=DEFAULT_PATH)
        hbox1.Add(self.tc_path, proportion=1)
        bt_browse = wx.Button(panel, label="Browse")
        bt_browse.Bind(wx.EVT_BUTTON, self.OnBrowse)
        hbox1.Add(bt_browse, flag=wx.LEFT, border=10)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        sample = wx.Bitmap("cache/images/mycat.png", wx.BITMAP_TYPE_ANY)
        self.sb_sample = wx.StaticBitmap(panel, wx.ID_ANY, sample)
        self.hbox2.Add(self.sb_sample, proportion=1, flag=wx.EXPAND)
        vbox.Add(self.hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        bt_identify = wx.Button(panel, label="Identify")
        bt_identify.Bind(wx.EVT_BUTTON, self.OnIdentify)
        hbox3.Add(bt_identify, flag=wx.RIGHT, border=10)
        self.st_identity = wx.StaticText(panel, label=DEFAULT_ID)
        hbox3.Add(self.st_identity, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        panel.SetSizer(vbox)

    def ScaleBitmap(self, bitmap, width, height):
        image = bitmap.ConvertToImage()
        # Retain the aspect ratio
        w = image.GetWidth()
        h = image.GetHeight()
        oar = w/h # Original aspect ratio
        par = width/height # Proposed aspect ratio
        if oar > par:
            height = width / oar
        else:
            width = height * oar
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return(result)

    def OnBrowse(self, event):
        dlg = wx.FileDialog(self,
                            message="Choose a file",
                            defaultDir=self.images_dir, 
                            defaultFile="",
                            wildcard=WILDCARD,
                            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            if len(paths):
                # Display path in text control.
                self.tc_path.SetValue(paths[0])
                # Update the image display.
                sample = wx.Bitmap(paths[0], wx.BITMAP_TYPE_ANY)
                sample = self.ScaleBitmap(sample, 500, 300)
                self.sb_sample.SetBitmap(sample)
                # Update the Identification text.
                self.st_identity.SetLabel(DEFAULT_ID)
                # Recenter the image
                self.hbox2.Layout()

    def OnIdentify(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = "cache/images/sample.jpg"
        results = subprocess.check_output(["ml", "ocr", "azcv", path])
        del(wait)
        r = results.decode("utf-8").split("\n")[0].split(",")
        certainty = r[0]
        identified = " or".join(r[1:len(r)])
        self.st_identity.SetLabel(f"{identified} [{certainty}]")
	# Show all identifications on the command line.
        print(path)
        print(results.decode("utf-8"))

    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
                               "Do you really want to close MLHub " + MODEL +"?",
                               "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
        
def main():
    app = wx.App()
    mlhub = MLHub(None, title='MLHub: ' + MODEL)
    mlhub.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
