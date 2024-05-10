import random

from sneck.classes.position import Position
from sneck.classes.snake import Snake
from sneck.classes.text import Text
from sneck.enumerations import Direction, TextType
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class PlayingState(GameState):
    fruit = Text("◉", TextType.FRUIT)

    def __init__(self, game: GameContext):
        # game aliases
        self._game = game
        self._board = game.output.board
        self._score_bar_text = game.output.score_bar_text
        self._score_board_data = game.score_board_data
        self._display = game.display

        self._snake = Snake(position=self._board.get_center())
        self._game.score = 0
        self._game_over = False

        self._initialise_game()

    def handle_input(self, key: str):
        match key:
            case "H":
                self._snake.set_direction(Direction.LEFT)
            case "J":
                self._snake.set_direction(Direction.DOWN)
            case "K":
                self._snake.set_direction(Direction.UP)
            case "L":
                self._snake.set_direction(Direction.RIGHT)

    def run(self):
        self._snake.update_head_position()
        self._write_score_bar_text()
        self._check_for_collision()

        if self._game_over:
            self._game.transition_to_game_over()
            return

        self._write_head_to_board()
        self._cleanup_tail()

    def _initialise_game(self):
        self._display.load_default_theme()
        self._board.clear()
        self._board.write_border()
        self._add_fruit_to_board()
        self._write_head_to_board()

    def _add_fruit_to_board(self) -> None:
        rows, cols = self._board.get_dimensions()

        while True:
            random_cell = Position(
                random.randint(0, rows - 1), random.randint(0, cols - 1)
            )
            cell_value = self._board.get_cell(random_cell)
            if (
                cell_value == Text(" ")
                and random_cell != self._snake.get_head_position()
            ):
                self._board.write_cell(random_cell, self.fruit)
                return

    def _write_head_to_board(self) -> None:
        head_position = self._snake.get_head_position()
        self._board.write_cell(head_position, self._snake._head_char)

    def _cleanup_tail(self) -> None:
        if len(self._snake.body_positions) > self._snake.get_length():
            self._board.erase_cell(self._snake.body_positions.pop(0))

    def _write_score_bar_text(self) -> None:
        text_width = self._board.get_width()
        current_high_score = self._score_board_data.entries[0].score

        high_score_text = f"HIGH: {current_high_score:04d}"

        score_text = f"SCORE: {self._game.score:04d}".ljust(
            text_width - len(high_score_text)
        )

        score_bar_text = score_text + high_score_text + "\n"

        self._score_bar_text.value = score_bar_text

    def _increase_score(self):
        score_per_fruit = 10
        theme_change_threshold = 100

        self._game.score += score_per_fruit
        if self._game.score % theme_change_threshold == 0:
            self._display.next_theme()

    def _check_for_collision(self) -> None:
        head_position = self._snake.get_head_position()
        target_cell_value = self._board.get_cell(head_position)

        if target_cell_value == Text(" "):
            return
        elif target_cell_value == self.fruit:
            self._increase_score()
            self._snake.increase_length()
            self._add_fruit_to_board()
        else:
            self._game_over = True
