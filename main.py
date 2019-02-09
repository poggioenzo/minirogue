#!/usr/bin/env python3


from curses import wrapper
from framework.gameobject import *
from framework.board import *
from framework.gamemanager import *
import curses
import sys

def main(stdscr):
    stdscr.clear()

    if curses.COLS < MAP_WIDTH - 1 or curses.LINES < MAP_HEIGHT - 1:
        print("Terminal Too Small", file=sys.stderr)
        sys.exit(-1)

    curses.curs_set(0)
    win = curses.newwin(MAP_HEIGHT, MAP_WIDTH, WIN_Y, WIN_X)
    win.keypad(True)

    doorA = Door(18, 39)
    doorB = Door(55, 60)

    roomA = Room(0, 0, 30, 40, [doorA])
    roomB = Room(50, 60, 10, 10, [doorB])

    board = Board([roomA, roomB], [(doorA, doorB)])

    Manager = GameManager(board)
   # Manager.printBoard()
    y, x = 10, 1
    while True:
        win.erase()

        for _, gameObject in board.all.items():
            win.addstr(gameObject.y, gameObject.x, gameObject.sym)

        win.addstr(y, x, "\u263b")
        win.refresh()
        key = win.getch()
        if key == curses.KEY_LEFT:
            if x > 1:
                x -= 1
        elif key == curses.KEY_RIGHT:
            if x < MAP_WIDTH - 2:
                x += 1
            x += 1
        elif key == curses.KEY_UP:
            if y > 1:
                y -= 1
        elif key == curses.KEY_DOWN:
            if y < MAP_HEIGHT - 2:
                y += 1


if __name__ == "__main__":
    wrapper(main)
