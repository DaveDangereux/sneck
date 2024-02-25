import curses
import time

from .board import Board


class Game:
    fps = 7.0

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self._board = Board()

    def run(self):
        while True:
            self.stdscr.clear()
            self.process_user_input()
            self.display_board()
            time.sleep(1.0 / self.fps)

    def display_board(self):
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
        # TODO: Figure out why this is flickering
        self.stdscr.addstr(str(self._board))
        self.stdscr.refresh()

    def process_user_input(self) -> None:
        try:
            key = self.stdscr.getkey()
        except Exception:
            key = ""

        if key == "q":
            curses.endwin()
            exit(0)
        elif key in "hjkl":
            self.stdscr.addstr(key)
