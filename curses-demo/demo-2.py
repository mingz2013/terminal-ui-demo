# -*- coding: utf-8 -*-
"""
@FileName: demo-2
@Time: 2020/7/18 10:58
@Author: zhaojm

Module Description

"""


from curses import wrapper

def main(stdscr):
    # clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i - 10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))


    stdscr.refresh()
    stdscr.getkey()

wrapper(main)