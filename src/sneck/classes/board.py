from sneck.classes.position import Position
from sneck.classes.text import Text


class Board:
    _board: list[list[Text]]

    def __init__(self, rows, cols):
        # TODO: Prevent these values from exceeding the terminal dimensions
        self._rows = rows
        self._cols = cols
        self.clear()

    def __getitem__(self, key: int) -> list[Text]:
        return self._board[key]

    def __setitem__(self, key: int, value: list[Text]) -> None:
        self._board[key] = value

    def clear(self):
        self._board = [
            [Text(" ") for _ in range(self._cols)] for _ in range(self._rows)
        ]

    def get_center(self) -> Position:
        return Position(self._rows // 2, self._cols // 2)

    def get_dimensions(self) -> tuple[int, int]:
        return self._rows, self._cols

    def get_width(self) -> int:
        return self._cols

    def get_lines(self):
        for row in self._board:
            yield row

    def write_cell(self, position: Position, text: Text) -> None:
        self._board[position.row][position.col] = text

    def get_cell(self, position: Position) -> Text:
        return self._board[position.row][position.col]

    def erase_cell(self, position: Position) -> None:
        self._board[position.row][position.col] = Text(" ")
