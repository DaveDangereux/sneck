import curses
import time

from .board import Board
from .snake import Snake


class Game:
    fps = 7

    def __init__(self):
        self.stdscr = curses.initscr()
        self.configure_curses()

        self._board = Board()
        self._snake = Snake(position=self._board.get_center())

    def configure_curses(self):
        curses.noecho()
        curses.curs_set(0)
        self.stdscr.nodelay(True)

    def run(self):
        while True:
            self.stdscr.clear()
            self.process_user_input()
            self.update_board()
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

    def update_board(self):
        self.update_snake()

    def update_snake(self):
        row = self._snake.position.row
        col = self._snake.position.col
        head = self._snake.head
        self._board.write_cell(row, col, head)
