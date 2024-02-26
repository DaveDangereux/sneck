from copy import copy

from ..assets.ascii_chars import box_chars
from .position import Position


class Board:
    def __init__(self, rows=25, columns=50):
        # TODO: Prevent these values from exceeding the terminal dimensions
        self._rows = rows
        self._columns = columns
        self._board = self._make_board()
        self._board_string = ""
        self._refresh_board_string()

    def __str__(self):
        return self._board_string

    def get_center(self) -> Position:
        return Position(self._rows // 2, self._columns // 2)

    def write_cell(self, position: Position, char: str) -> None:
        self._board[position.row][position.col] = char
        self._refresh_board_string()

    def _make_row(self, left_char: str, middle_char: str, right_char: str) -> list[str]:
        row = [middle_char] * self._columns
        row[0] = left_char
        row[-1] = right_char
        return row

    def _make_board(self) -> list[list[str]]:
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

        board = []
        for _ in range(self._rows):
            board.append(copy(middle_row))
        board[0] = top_row
        board[-1] = bottom_row

        return board

    def _refresh_board_string(self) -> None:
        self._board_string = "\n".join(["".join(row) for row in self._board])
