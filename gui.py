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
import re

MODEL = "Azure Computer Vision"
CMD_OCR = ["ml", "ocr", "azcv"]
CMD_TAGS = ["ml", "tags", "azcv"]
CMD_DESCRIBE = ["ml", "describe", "azcv"]
CMD_LANDMARKS = ["ml", "landmarks", "azcv"]
CMD_FACES = ["ml", "faces", "azcv"]
CMD_CELEBRITIES = ["ml", "celebrities", "azcv"]

DEFAULT_PATH = "Enter a local path to an image (jpg, png) file"
DEFAULT_IMAGE = os.path.join(os.getcwd(), "cache/images/mycat.png")
DEFAULT_ID = "Results will appear here ..."

NO_RESULTS = "No results returned from the model."

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
        sample = wx.Bitmap(DEFAULT_IMAGE, wx.BITMAP_TYPE_ANY)
        sample = self.ScaleBitmap(sample, 500, 300)
        self.sb_sample = wx.StaticBitmap(panel, wx.ID_ANY, sample)
        self.hbox2.Add(self.sb_sample, flag=wx.EXPAND)
        self.hbox2.Add((10, -1))
        self.st_results = wx.StaticText(panel, label=DEFAULT_ID)
        self.hbox2.Add(self.st_results, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(self.hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # OCR
        bt_ocr = wx.Button(panel, label="OCR")
        bt_ocr.Bind(wx.EVT_BUTTON, self.OnOCR)
        hbox3.Add(bt_ocr, flag=wx.RIGHT, border=10)
        # TAGS
        bt_tags = wx.Button(panel, label="Tags")
        bt_tags.Bind(wx.EVT_BUTTON, self.OnTAGS)
        hbox3.Add(bt_tags, flag=wx.RIGHT, border=10)
        # DESCRIBE
        bt_describe = wx.Button(panel, label="Describe")
        bt_describe.Bind(wx.EVT_BUTTON, self.OnDESCRIBE)
        hbox3.Add(bt_describe, flag=wx.RIGHT, border=10)
        # LANDMARKS
        bt_landmarks = wx.Button(panel, label="Landmarks")
        bt_landmarks.Bind(wx.EVT_BUTTON, self.OnLANDMARKS)
        hbox3.Add(bt_landmarks, flag=wx.RIGHT, border=10)
        # FACES
        bt_faces = wx.Button(panel, label="Faces")
        bt_faces.Bind(wx.EVT_BUTTON, self.OnFACES)
        hbox3.Add(bt_faces, flag=wx.RIGHT, border=10)
        # CELEBRITIES
        bt_celebrities = wx.Button(panel, label="Celebrities")
        bt_celebrities.Bind(wx.EVT_BUTTON, self.OnCELEBRITIES)
        hbox3.Add(bt_celebrities, flag=wx.RIGHT, border=10)
        # Add to the panel.
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
                self.st_results.SetLabel(DEFAULT_ID)
                # Recenter the image
                self.hbox2.Layout()

    def OnOCR(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = DEFAULT_IMAGE
        cmd = CMD_OCR.copy()
        cmd.append(path)
	# Show the command line.
        print("$ " + " ".join(cmd))
        results = subprocess.check_output(cmd)
        r = re.sub('^.*?,', '', re.sub('\n.*?,', '\n', results.decode("utf-8")))
        self.st_results.SetLabel(r)
        self.hbox2.Layout()
	# Show the command line results.
        print(results.decode("utf-8"))
        del(wait)

    def OnTAGS(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = DEFAULT_IMAGE
        cmd = CMD_TAGS.copy()
        cmd.append(path)
	# Show the command line.
        print("$ " + " ".join(cmd))
        results = subprocess.check_output(cmd)
        if len(results) == 0:
            self.st_results.SetLabel(NO_RESULTS)
        else:
            r = re.sub(r'^(.*?),', r'[\1] ', re.sub(r'\n(.*?),', r'\n[\1] ', results.decode("utf-8")))
            self.st_results.SetLabel(r)
        self.hbox2.Layout()
	# Show the command line results.
        print(results.decode("utf-8"))
        del(wait)

    def OnDESCRIBE(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = DEFAULT_IMAGE
        cmd = CMD_DESCRIBE.copy()
        cmd.append(path)
	# Show the command line.
        print("$ " + " ".join(cmd))
        results = subprocess.check_output(cmd)
        if len(results) == 0:
            self.st_results.SetLabel(NO_RESULTS)
        else:
            r = re.sub(r'^(.*?),', r'[\1] ', re.sub(r'\n(.*?),', r'\n[\1] ', results.decode("utf-8")))
            self.st_results.SetLabel(r)
        self.hbox2.Layout()
	# Show the command line results.
        print(results.decode("utf-8"))
        del(wait)

    def OnLANDMARKS(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = DEFAULT_IMAGE
        cmd = CMD_LANDMARKS.copy()
        cmd.append(path)
	# Show the command line.
        print("$ " + " ".join(cmd))
        results = subprocess.check_output(cmd)
        if len(results) == 0:
            self.st_results.SetLabel(NO_RESULTS)
        else:
            r = re.sub(r'^(.*?),', r'[\1] ', re.sub(r'\n(.*?),', r'\n[\1] ', results.decode("utf-8")))
            self.st_results.SetLabel(r)
        self.hbox2.Layout()
	# Show the command line results.
        print(results.decode("utf-8"))
        del(wait)

    def OnFACES(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = DEFAULT_IMAGE
        cmd = CMD_FACES.copy()
        cmd.append(path)
	# Show the command line.
        print("$ " + " ".join(cmd))
        results = subprocess.check_output(cmd)
        if len(results) == 0:
            self.st_results.SetLabel(NO_RESULTS)
        else:
            r = re.sub(r'^(.*?),', r'[\1] ', re.sub(r'\n(.*?),', r'\n[\1] ', results.decode("utf-8")))
            self.st_results.SetLabel(r)
        self.hbox2.Layout()
	# Show the command line results.
        print(results.decode("utf-8"))
        del(wait)

    def OnCELEBRITIES(self, event):
        wait = wx.BusyCursor()
        path = self.tc_path.GetValue()
        if path == DEFAULT_PATH:
            path = DEFAULT_IMAGE
        cmd = CMD_CELEBRITIES.copy()
        cmd.append(path)
	# Show the command line.
        print("$ " + " ".join(cmd))
        results = subprocess.check_output(cmd)
        if len(results) == 0:
            self.st_results.SetLabel(NO_RESULTS)
        else:
            r = re.sub(r'^(.*?),', r'[\1] ', re.sub(r'\n(.*?),', r'\n[\1] ', results.decode("utf-8")))
            self.st_results.SetLabel(r)
        self.hbox2.Layout()
	# Show the command line results.
        print(results.decode("utf-8"))
        del(wait)

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
