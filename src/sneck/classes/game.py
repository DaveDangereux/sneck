import curses
import time

from .board import Board
from .direction import Direction
from .snake import Snake


class Game:
    def __init__(self, fps=7):
        self._frame_duration = 1.0 / 7
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
            self._snake.move()
            self.add_snake_to_board()
            self.display_board()
            time.sleep(self._frame_duration)

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

        match key:
            case "q":
                curses.endwin()
                exit(0)
            case "h":
                self._snake.set_direction(Direction.LEFT)
            case "j":
                self._snake.set_direction(Direction.DOWN)
            case "k":
                self._snake.set_direction(Direction.UP)
            case "l":
                self._snake.set_direction(Direction.RIGHT)

    def add_snake_to_board(self):
        position = self._snake.get_position()
        head = self._snake.head

        self._board.write_cell(position, head)
