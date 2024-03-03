import random
import time

from ...assets.ascii_chars import fruit
from ...enumerations.direction import Direction
from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext
from ...tools import painter
from ..position import Position
from ..snake import Snake


class PlayingState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager

        self.game = state_manager.game
        self.game.score = 0
        self.game_over = False
        self.snake = Snake(position=self.game.board.get_center())

        self.game.screen.enable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        painter.paint_border(self.game.board)
        self._add_fruit_to_board()

        while self.state_manager.state == self:
            self._process_user_input()
            self.snake.update_head_position()
            self._check_for_collision()
            if self.game_over:
                self.state_manager.transition_to_game_over()
                return
            self._update_board()
            time.sleep(self.game.frame_duration)

    def _display_score_bar(self) -> None:
        text_width = self.game.board.get_width()
        high_score_text = f"HIGH: {self.game.score_board_data.entries[0].score:04d}"
        score_text = f"SCORE: {self.game.score:04d}".ljust(
            text_width - len(high_score_text)
        )
        score_bar_text = score_text + high_score_text + "\n"

        board_rows, board_cols = self.game.board.get_dimensions()
        col_offset = (self.game.screen._cols - board_cols) // 2
        row_offset = (self.game.screen._rows - board_rows) // 2 - 1

        self.game.screen.add_string(
            row_offset, col_offset, score_bar_text, self.game.screen.YELLOW
        )

    def _check_for_collision(self) -> None:
        head_position = self.snake.get_head_position()
        target_cell_value = self.game.board.get_cell(head_position)

        if target_cell_value == " ":
            return
        elif target_cell_value == fruit:
            self._add_fruit_to_board()
            self.snake.increase_length()
            self.game.score += 10
        else:
            self.game_over = True

    def _update_board(self) -> None:
        self._write_head_to_board()
        self._cleanup_tail()
        self.game.screen.add_board(self.game.board)
        self._display_score_bar()
        self.game.screen.refresh()

    def _cleanup_tail(self) -> None:
        if len(self.snake.body_positions) > self.snake.get_length():
            self.game.board.erase_cell(self.snake.body_positions.pop(0))

    def _add_fruit_to_board(self) -> None:
        rows, cols = self.game.board.get_dimensions()

        while True:
            random_cell = Position(
                random.randint(0, rows - 1), random.randint(0, cols - 1)
            )
            cell_value = self.game.board.get_cell(random_cell)
            if cell_value == " " and random_cell != self.snake.get_head_position():
                self.game.board.write_cell(random_cell, fruit)
                return

    def _write_head_to_board(self) -> None:
        head_position = self.snake.get_head_position()
        self.game.board.write_cell(head_position, self.snake.head_char)

    def _process_user_input(self) -> None:
        try:
            key = self.game.screen.get_key().upper()
        except Exception:
            key = ""

        match key:
            case "H":
                self.snake.set_direction(Direction.LEFT)
            case "J":
                self.snake.set_direction(Direction.DOWN)
            case "K":
                self.snake.set_direction(Direction.UP)
            case "L":
                self.snake.set_direction(Direction.RIGHT)
