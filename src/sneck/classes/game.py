from ..assets.ascii_chars import box_chars, fruit, snake_chars
from .board import Board
from .renderer import Renderer
from .state_manager import StateManager


class Game:
    def __init__(self, fps=8):
        self.game_counter = 0
        self.score = 0
        self.frame_duration = 1.0 / fps

        self.board = Board()
        self.renderer = Renderer()
        self.state_manager = StateManager(self)

    def run(self) -> None:
        while True:
            self.state_manager.run()

    def draw_board_to_screen(self) -> None:
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
        board_rows, board_cols = self.board.get_dimensions()
        col_offset = (self.renderer.cols - board_cols) // 2
        row_offset = (self.renderer.rows - board_rows) // 2

        for row_index, row in enumerate(self.board.get_lines()):
            for char_index, char in enumerate(row):
                colour = self.renderer.WHITE

                if char in box_chars.values():
                    colour = self.renderer.MAGENTA
                elif char in snake_chars.values():
                    colour = self.renderer.GREEN
                elif char is fruit:
                    colour = self.renderer.RED

                self.renderer.add_char(
                    row_index + row_offset, char_index + col_offset, char, colour
                )

    def draw_score_to_screen(self) -> None:
        score_text = f"Score: {self.score:03d}"
        formatted_score_text = self._right_justify_text(score_text) + "\n"

        board_rows, board_cols = self.board.get_dimensions()
        col_offset = (self.renderer.cols - board_cols) // 2
        row_offset = (self.renderer.rows - board_rows) // 2 - 1

        self.renderer.add_string(
            row_offset, col_offset, formatted_score_text, self.renderer.YELLOW
        )

    def _right_justify_text(self, text: str) -> str:
        _, width = self.board.get_dimensions()
        left_space = " " * (width - len(text))
        return left_space + text
