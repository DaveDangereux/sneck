import curses
import random
import time

from .board import Board
from .direction import Direction
from .snake import Snake


class Game:
    _game_counter = 0

    def __init__(self, fps=9):
        self._frame_duration = 1.0 / fps

        self._board = Board()
        self._snake = Snake(initial_position=self._board.get_center())
        self._stdscr = curses.initscr()

        curses.noecho()
        curses.curs_set(0)
        self._stdscr.nodelay(True)

    def run(self) -> None:
        while True:
            self._game_counter += 1
            self._stdscr.clear()
            self._process_snake_graphic()
            self._draw_board_to_screen()
            time.sleep(self._frame_duration)
            self._process_user_input()
            self._snake.move()

    def _process_snake_graphic(self) -> None:
        if self._game_counter > self._snake.get_length():
            old_tail_position = self._snake.get_old_tail_position()
            self._board.write_cell(old_tail_position, " ")

        head_position = self._snake.get_head_position()
        head_char = self._snake.head_char
        self._board.write_cell(head_position, head_char)

    def _draw_board_to_screen(self) -> None:
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
        self._stdscr.addstr(str(self._board))
        self._stdscr.refresh()

    def _process_user_input(self) -> None:
        try:
            key = self._stdscr.getkey()
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
