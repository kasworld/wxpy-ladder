#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015 SeukWon Kang (kasworld@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# generated by wxGlade 0.6.3 on Sat Dec  5 17:45:08 2009

import wx
import random

# begin wxGlade: extracode
# end wxGlade


class LadderControl(wx.Control):

    def __init__(self, *args, **kwds):
        wx.Control.__init__(self, *args, **kwds)
        self.Bind(wx.EVT_PAINT, self._OnPaint)
        self.Bind(wx.EVT_SIZE, self._OnSize)
        self.setPlayerNum(10)

    def _OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.SetBackground(wx.Brush("White", wx.SOLID))
        dc.Clear()
        size = self.GetClientSizeTuple()
        unitx, unity = float(
            size[0]) / self.playernum, float(size[1]) / self.ladderlen
        if not self.showhint:
            dc.SetPen(wx.Pen("Black", 2))
            for x in range(self.playernum):
                dc.DrawLine(
                    unitx * x + unitx / 2, 0, unitx * x + unitx / 2, size[1])
        else:
            plpos = range(self.playernum)
            for y in range(self.ladderlen + 1):
                for x in range(self.playernum):
                    pl = plpos[x]  # 지금 그려야 하는 플레이어.
                    dc.SetPen(wx.Pen(self.playercolors[pl], 4))
                    dc.DrawLine(x * unitx + unitx / 2, y * unity - unity /
                                2, x * unitx + unitx / 2, y * unity + unity / 2)
                for x in range(self.playernum):
                    if y < self.ladderlen and x < self.playernum - 1 and self.steps[y][x]:
                        plpos[x], plpos[x + 1] = plpos[x + 1], plpos[x]

            plpos = range(self.playernum)
            for y in range(self.ladderlen + 1):
                for x in range(self.playernum):
                    if y < self.ladderlen and x < self.playernum - 1 and self.steps[y][x]:
                        plpos[x], plpos[x + 1] = plpos[x + 1], plpos[x]
                        dc.SetPen(wx.Pen(self.playercolors[plpos[x]], 2))
                        dc.DrawLine(x * unitx + unitx / 2, y * unity + unity / 2 -
                                    2, (x + 1) * unitx + unitx / 2, y * unity + unity / 2 - 2)
                        dc.SetPen(wx.Pen(self.playercolors[plpos[x + 1]], 2))
                        dc.DrawLine(x * unitx + unitx / 2, y * unity + unity / 2 +
                                    2, (x + 1) * unitx + unitx / 2, y * unity + unity / 2 + 2)

    def _OnSize(self, evt):
        self.Refresh(False)
        self.Update()

    def setPlayerNum(self, num):
        self.showhint = False
        self.playernum = num
        self.ladderlen = self.playernum * 4
        self.makeLadder()

    def play(self):
        self.showhint = True
        self.playercolors = []
        for i in range(self.playernum):
            self.playercolors.append(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),))
        start = range(self.playernum)
        for b in self.steps:
            for c, pos in zip(b, range(len(b))):
                if c:
                    start[pos], start[pos + 1] = start[pos + 1], start[pos]
        # print start
        self.playercolors
        self.Refresh(False)
        return start, self.playercolors

    def makeLadder(self):
        self.steps = []
        for y in range(self.ladderlen):
            self.steps.append([])
            for x in range(self.playernum - 1):
                hbar = random.choice([0, 1])
                if hbar and (x >= 1 and self.steps[y][x - 1]) or (y >= 1 and self.steps[y - 1][x]):
                    hbar = 0
                self.steps[y].append(hbar)


class MyFrame(wx.Frame):

    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.maxplayernum = 100
        self.playernum = 10
        self.slider_1 = wx.Slider(
            self, -1, self.playernum, 2, self.maxplayernum, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.button_1 = wx.Button(self, -1, "Set player num")
        self.buttonPlay = wx.Button(self, -1, "Play")
        self.playername = []
        self.playresult = []
        for a in range(self.maxplayernum):
            self.playername.append(wx.TextCtrl(self, -1, "p%d" % a))
            self.playresult.append(wx.TextCtrl(self, -1, "r%d" % a))

        self.laddergrid = LadderControl(self, -1)
        self.laddergrid.setPlayerNum(self.playernum)

        self.__set_properties()
        self.__do_layout()
        self.reset_playernum()

        self.Bind(wx.EVT_BUTTON, self.btn_setplayernum, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.btn_doPlay, self.buttonPlay)

        # begin wxGlade: MyFrame.__init__
        # end wxGlade

    def __set_properties(self):
        self.SetTitle("wxLadderGame")
        # begin wxGlade: MyFrame.__set_properties
        # end wxGlade

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.slider_1, 3, wx.EXPAND, 0)
        sizer_4.Add(self.button_1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.buttonPlay, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        for a in range(self.maxplayernum):
            sizer_2.Add(self.playername[a], 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.laddergrid, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, self.playernum * 2, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        for a in range(self.maxplayernum):
            sizer_3.Add(self.playresult[a], 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

        # begin wxGlade: MyFrame.__do_layout
        # end wxGlade

    def reset_playernum(self):
        for a in range(self.maxplayernum):
            self.playername[a].Show(a < self.playernum)
            self.playername[a].SetBackgroundColour("White")
            self.playername[a].ChangeValue("p%d" % a)
            self.playresult[a].Show(a < self.playernum)
            self.playresult[a].SetBackgroundColour("White")
            self.playresult[a].ChangeValue("r%d" % a)
        self.laddergrid.setPlayerNum(self.playernum)
        # sizer_1.Fit(self)
        self.Layout()

    def btn_setplayernum(self, event):  # wxGlade: MyFrame.<event_handler>
        self.playernum = self.slider_1.GetValue()
        self.reset_playernum()

    def btn_doPlay(self, event):
        result, cols = self.laddergrid.play()
        for i in range(self.playernum):
            self.playername[i].SetBackgroundColour(cols[i])
            self.playresult[i].SetBackgroundColour(cols[result[i]])
            pn = self.playername[result[i]].GetValue()
            rn = self.playresult[i].GetValue()
            if not rn.startswith(pn):
                self.playresult[i].ChangeValue("%s:%s" % (pn, rn))

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
