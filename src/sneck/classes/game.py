import curses
import time

from .board import Board
from .direction import Direction
from .snake import Snake


class Game:
    game_counter = 1

    def __init__(self, fps=1):
        self._frame_duration = 1.0 / fps
        self.stdscr = curses.initscr()
        self.configure_curses()

        self._board = Board()
        self._snake = Snake(initial_position=self._board.get_center())

    def configure_curses(self):
        curses.noecho()
        curses.curs_set(0)
        self.stdscr.nodelay(True)

    def run(self):
        self.draw_snake_head()
        while True:
            self.stdscr.clear()
            self.remove_old_tail()
            self.draw_snake_head()
            self.display_board()
            self._snake.move()
            time.sleep(self._frame_duration)
            self.process_user_input()
            self.game_counter += 1

    def display_board(self):
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
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

    def remove_old_tail(self):
        if self.game_counter > self._snake.get_length():
            old_tail_position = self._snake.get_old_tail_position()
            self._board.write_cell(old_tail_position, " ")

    def draw_snake_head(self):
        head_position = self._snake.get_head_position()
        head = self._snake.head
        self._board.write_cell(head_position, head)
