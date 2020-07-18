# -*- coding: utf-8 -*-
"""
@FileName: demo-2
@Time: 2020/7/18 11:16
@Author: zhaojm

Module Description

"""


import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text('hello world')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()