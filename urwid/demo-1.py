# -*- coding: utf-8 -*-
"""
@FileName: demo-1
@Time: 2020/7/18 11:12
@Author: zhaojm

Module Description

"""


import urwid

txt = urwid.Text("hello world")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()