from ..assets.ascii_chars import box_chars


class Board:
    def __init__(self, width=40, height=20):
        # TODO: Prevent these values from exceeding the terminal dimensions
        self._width = width
        self._height = height
        self._board = self.make_board()
        self._stringified_board = self.stringify_board()

    def __str__(self):
        return self._stringified_board

    def make_row(self, left_char: str, middle_char: str, right_char: str) -> list[str]:
        row = [middle_char] * self._width
        row[0] = left_char
        row[-1] = right_char
        return row

    def make_board(self) -> list[list[str]]:
        top_row = self.make_row(
            box_chars["top_left"], box_chars["horizontal_bar"], box_chars["top_right"]
        )
        middle_row = self.make_row(
            box_chars["vertical_bar"], " ", box_chars["vertical_bar"]
        )
        bottom_row = self.make_row(
            box_chars["bottom_left"],
            box_chars["horizontal_bar"],
            box_chars["bottom_right"],
        )

        board = [middle_row] * self._height
        board[0] = top_row
        board[-1] = bottom_row

        return board

    def stringify_board(self) -> str:
        return "\n".join(["".join(row) for row in self._board])
