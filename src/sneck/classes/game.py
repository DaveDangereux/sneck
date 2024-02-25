import curses
import time

from .board import Board


class Game:
    def __init__(self):
        self.stdscr = curses.initscr()
        self._board = Board()

    def run(self):
        self.print_board()
        time.sleep(2)
        curses.endwin()

    def print_board(self):
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
        self.stdscr.addstr(str(self._board))
        self.stdscr.refresh()
