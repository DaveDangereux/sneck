import random
import time

from sneck.assets.ascii_chars import fruit
from sneck.classes.position import Position
from sneck.classes.snake import Snake
from sneck.classes.text import Text
from sneck.enumerations import Direction, TextType
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class PlayingState(GameState):
    def __init__(self, game: GameContext):
        self.game = game

        self.game.score = 0
        self.game_over = False
        self.snake = Snake(position=self.game.board.get_center())

        self.game.screen.palette.load_default_theme()
        self.game.screen.enable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        self.game.board.write_border()
        self._add_fruit_to_board()
        self._update_board()

        while self.game.state == self:
            self._process_user_input()
            self.snake.update_head_position()
            self._check_for_collision()
            if self.game_over:
                self.game.transition_to_game_over()
                return
            self._update_board()
            time.sleep(self.game.frame_duration)

    def _update_board(self) -> None:
        self._write_head_to_board()
        self._cleanup_tail()
        self.game.screen.add_board(self.game.board)
        self._update_score_bar()
        self.game.screen.refresh()

    def _cleanup_tail(self) -> None:
        if len(self.snake.body_positions) > self.snake.get_length():
            self.game.board.erase_cell(self.snake.body_positions.pop(0))

    def _write_head_to_board(self) -> None:
        head_position = self.snake.get_head_position()
        self.game.board.write_cell(head_position, self.snake._head_char)

    def _update_score_bar(self) -> None:
        text_width = self.game.board.get_width()
        current_high_score = self.game.score_board_data.entries[0].score

        high_score_text = f"HIGH: {current_high_score:04d}"

        score_text = f"SCORE: {self.game.score:04d}".ljust(
            text_width - len(high_score_text)
        )

        score_bar_text = score_text + high_score_text + "\n"

        self.game.screen.add_score_bar(Text(score_bar_text, TextType.SCORE))

    def _check_for_collision(self) -> None:
        head_position = self.snake.get_head_position()
        target_cell_value = self.game.board.get_cell(head_position)

        if target_cell_value == Text(" "):
            return
        elif target_cell_value == fruit:
            self._add_fruit_to_board()
            self.snake.increase_length()
            self.game.score += 10
            if self.game.score % 200 == 0:
                self.game.screen.palette.load_next_theme()
        else:
            self.game_over = True

    def _add_fruit_to_board(self) -> None:
        rows, cols = self.game.board.get_dimensions()

        while True:
            random_cell = Position(
                random.randint(0, rows - 1), random.randint(0, cols - 1)
            )
            cell_value = self.game.board.get_cell(random_cell)
            if (
                cell_value == Text(" ")
                and random_cell != self.snake.get_head_position()
            ):
                self.game.board.write_cell(random_cell, fruit)
                return

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
