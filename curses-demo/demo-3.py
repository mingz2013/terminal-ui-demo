# -*- coding: utf-8 -*-
"""
@FileName: demo-3
@Time: 2020/7/18 11:03
@Author: zhaojm

Module Description

"""


from curses import wrapper
import curses


def main(stdscr):
    """
    """

    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    

wrapper(main)
