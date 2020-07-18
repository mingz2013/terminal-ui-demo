# -*- coding: utf-8 -*-
"""
@FileName: demo-1
@Time: 2020/7/18 10:48
@Author: zhaojm

Module Description

"""


import curses



# 初始化
stdscr = curses.initscr()
# 屏幕停止输出无关内容
curses.noecho()
# cbreak模式，立即响应键，不需要按enter键。称为cbreak模式，与通常的缓冲输入模式相反。
curses.cbreak()

curses.nocbreak()
curses.echo()
curses.endwin()
