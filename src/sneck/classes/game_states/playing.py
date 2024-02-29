import random
import time

from ...assets.ascii_chars import fruit
from ...enumerations.direction import Direction
from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext
from ..position import Position
from ..snake import Snake


class PlayingState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game = state_manager.game

        self.snake = Snake(position=self.game.board.get_center())

    def run(self):
        self._reset_game_variables()
        self._place_fruit()

        while self.state_manager.state == self:
            # TODO: Fix bug where fruit is eaten too quickly and doesn't
            # respawn
            self.game.renderer.erase()
            self.game.game_counter += 1
            self._process_snake_graphic()
            self.game.draw_score_to_screen()
            self.game.draw_board_to_screen()
            self.game.renderer.refresh()
            time.sleep(self.game.frame_duration)
            self._process_user_input()
            self.snake.move()

    def _reset_game_variables(self):
        self.game.board.make_game_board()
        self.snake.reset_snake()
        self.game.game_counter = 0
        self.game.score = 0

    def _place_fruit(self) -> None:
        rows, cols = self.game.board.get_dimensions()

        while True:
            random_cell = Position(
                random.randint(0, rows - 1), random.randint(0, cols - 1)
            )
            cell_value = self.game.board.get_cell(random_cell)
            if cell_value == " ":
                self.game.board.write_cell(random_cell, fruit)
                return

    def _process_snake_graphic(self) -> None:
        game_counter = self.game.game_counter
        snake_length = self.snake.get_length()
        is_fully_moved_into_board = game_counter > snake_length

        if is_fully_moved_into_board:
            self._erase_old_tail()

        new_head_position = self.snake.get_head_position()
        head_char = self.snake.head_char
        target_cell_value = self.game.board.get_cell(new_head_position)
        target_cell_is_empty = target_cell_value == " "

        if not target_cell_is_empty:
            self._handle_collision(target_cell_value)

        self.game.board.write_cell(new_head_position, head_char)

    def _process_user_input(self) -> None:
        set_snake_direction = self.snake.set_direction

        try:
            key = self.game.renderer.get_key()
        except Exception:
            key = ""

        match key:
            case "q":
                self.game.renderer.stop()

                exit(0)
            case "h":
                set_snake_direction(Direction.LEFT)
            case "j":
                set_snake_direction(Direction.DOWN)
            case "k":
                set_snake_direction(Direction.UP)
            case "l":
                set_snake_direction(Direction.RIGHT)

    def _erase_old_tail(self):
        old_tail_position = self.snake.get_old_tail_position()
        self.game.board.write_cell(old_tail_position, " ")

    def _handle_collision(self, value: str) -> None:
        if value == fruit:
            self._place_fruit()
            self.snake.increase_length()
            self.game.score += 1
        else:
            self.state_manager.transition_to_game_over()
