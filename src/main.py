import curses

from random import choice, shuffle
from sort import *

def get_nums(stdscr):
    y, x = stdscr.getmaxyx()
    size = min(y, x) - 2
    result = []
    for i in range(size):
        result += [i + 2]
    return result

def display_nums(stdscr, nums, selected=-1):
    y, x = stdscr.getmaxyx()
    stdscr.clear()
    y_start = y - 1
    x_start = x - 2 * len(nums)
    for i in range(len(nums)):
        if selected == i:
            for j in range(nums[i]):
                stdscr.addstr(y_start - j, x_start + 2 * i, "x", curses.A_REVERSE)
        else:
            for j in range(nums[i]):
                stdscr.addstr(y_start - j, x_start + 2 * i, "x")
    stdscr.refresh()
    curses.napms(20)

def sort(so, stdscr, options, choice_i):
    so.sort_using(options[choice_i])
    display_nums(stdscr, so.arr)
    stdscr.addstr(0, 0, '[ENTER SPACE TO SORT AGAIN]')
    if stdscr.getch() == 32:
        sort(so, stdscr, options, choice_i)
    stdscr.clear()

def main(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(1)
    nums = get_nums(stdscr)
    so = SortObj(nums, stdscr, display_nums) 
    options = list(so.sa.keys())
    options += ['Quit']
    choice_i = 0
    while True:
        for i in range(len(options)):
            if i == choice_i:
                stdscr.addstr(i, 0, options[i], curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, options[i])
        key = stdscr.getch()
        if key == 259: # UP
            choice_i -= 1
            if choice_i < 0:
                choice_i = len(options) - 1
        if key == 258: # DOWN
            choice_i += 1
            if choice_i == len(options):
                choice_i = 0
        if key == 10 or key == 32: # ENTER/SPACE
            if options[choice_i] == 'Quit':
                break
            sort(so, stdscr, options, choice_i)
            

curses.wrapper(main)