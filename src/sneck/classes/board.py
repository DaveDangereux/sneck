from copy import copy

from ..assets.ascii_chars import box_chars
from .position import Position


class Board:
    def __init__(self, rows=18, cols=24):
        # TODO: Prevent these values from exceeding the terminal dimensions
        self._rows = rows
        self._cols = cols
        self._board = []
        self.make_title_screen()
        self._board_string = ""
        self._refresh_board_string()

    def __str__(self):
        return self._board_string

    def get_center(self) -> Position:
        return Position(self._rows // 2, self._cols // 2)

    def get_dimensions(self) -> tuple[int, int]:
        return self._rows, self._cols

    def get_lines(self):
        for row in self._board:
            yield row

    def write_cell(self, position: Position, char: str) -> None:
        self._board[position.row][position.col] = char
        self._refresh_board_string()

    def get_cell(self, position: Position) -> str:
        return self._board[position.row][position.col]

    def _make_row(self, left_char: str, middle_char: str, right_char: str) -> list[str]:
        row = [middle_char] * self._cols
        row[0] = left_char
        row[-1] = right_char
        return row

    def make_game_board(self) -> None:
        top_row = self._make_row(
            box_chars["top_left"], box_chars["horizontal_bar"], box_chars["top_right"]
        )
        middle_row = self._make_row(
            box_chars["vertical_bar"], " ", box_chars["vertical_bar"]
        )
        bottom_row = self._make_row(
            box_chars["bottom_left"],
            box_chars["horizontal_bar"],
            box_chars["bottom_right"],
        )

        self._board = []
        for _ in range(self._rows):
            self._board.append(copy(middle_row))
        self._board[0] = top_row
        self._board[-1] = bottom_row

    def make_title_screen(self):
        self.make_game_board()

        title_text = ["S N A K E", "Press any key to play"]
        self._centre_on_board(title_text)

    def _centre_on_board(self, text: list[str]) -> None: ...

    def make_game_over(self):
        self.make_game_board()

    def _refresh_board_string(self) -> None:
        self._board_string = "\n".join(["".join(row) for row in self._board]) + "\n"
