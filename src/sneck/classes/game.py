import curses
import random
import time

from ..assets.ascii_chars import fruit
from .board import Board
from .direction import Direction
from .position import Position
from .snake import Snake


class Game:
    _game_counter = 0
    _score = 0

    def __init__(self, fps=8):
        self._frame_duration = 1.0 / fps

        self._board = Board()
        self._snake = Snake(initial_position=self._board.get_center())
        self._stdscr = curses.initscr()

        curses.noecho()
        curses.curs_set(0)
        self._stdscr.nodelay(True)

    def run(self) -> None:
        self._place_fruit()

        while True:
            # TODO: Fix bug where fruit is eaten too quickly and doesn't
            # respawn
            self._game_counter += 1
            self._stdscr.clear()
            self._process_snake_graphic()
            self._draw_score_to_screen()
            self._draw_board_to_screen()
            self._stdscr.refresh()
            time.sleep(self._frame_duration)
            self._process_user_input()
            self._snake.move()

    def _process_snake_graphic(self) -> None:
        if self._game_counter > self._snake.get_length():
            old_tail_position = self._snake.get_old_tail_position()
            self._board.write_cell(old_tail_position, " ")

        head_position = self._snake.get_head_position()
        head_char = self._snake.head_char
        target_cell_value = self._board.get_cell(head_position)
        if target_cell_value != " ":
            self._handle_collision(target_cell_value)
        self._board.write_cell(head_position, head_char)

    def _draw_board_to_screen(self) -> None:
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
        self._stdscr.addstr(str(self._board))

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

    def _place_fruit(self) -> None:
        rows, cols = self._board.get_dimensions()

        while True:
            random_cell = Position(
                random.randint(0, rows - 1), random.randint(0, cols - 1)
            )
            cell_value = self._board.get_cell(random_cell)
            if cell_value == " ":
                self._board.write_cell(random_cell, fruit)
                return

    def _handle_collision(self, value: str) -> None:
        if value == fruit:
            self._place_fruit()
            self._snake.increase_length()
            self._score += 1
        else:
            self._handle_game_over()

    def _draw_score_to_screen(self) -> None:
        score_text = f"Score: {self._score:03d}"
        formatted_score_text = self._right_justify_text(score_text) + "\n"
        self._stdscr.addstr(formatted_score_text)

    def _right_justify_text(self, text: str) -> str:
        _, width = self._board.get_dimensions()
        left_space = " " * (width - len(text))
        return left_space + text

    def _handle_game_over(self) -> None:
        exit(0)
