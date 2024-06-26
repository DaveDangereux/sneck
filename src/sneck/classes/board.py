from sneck.classes.position import Position
from sneck.classes.text import Text
from sneck.enumerations import TextType


class Board:
    _BOX_CHARS = {
        "top_left": Text("╔", TextType.WALL),
        "top_right": Text("╗", TextType.WALL),
        "bottom_left": Text("╚", TextType.WALL),
        "bottom_right": Text("╝", TextType.WALL),
        "horizontal_bar": Text("═", TextType.WALL),
        "vertical_bar": Text("║", TextType.WALL),
    }

    _board: list[list[Text]]

    def __init__(self, rows: int, cols: int):
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

    def get_height(self) -> int:
        return self._rows

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

    def write_border(self) -> None:
        for row in self._board:
            row[0] = self._BOX_CHARS["vertical_bar"]
            row[-1] = self._BOX_CHARS["vertical_bar"]

        self._board[0] = [self._BOX_CHARS["horizontal_bar"] for _ in self._board[0]]
        self._board[0][0] = self._BOX_CHARS["top_left"]
        self._board[0][-1] = self._BOX_CHARS["top_right"]

        self._board[-1] = [self._BOX_CHARS["horizontal_bar"] for _ in self._board[0]]
        self._board[-1][0] = self._BOX_CHARS["bottom_left"]
        self._board[-1][-1] = self._BOX_CHARS["bottom_right"]

    def write_centre_text(self, lines: list[Text]) -> None:
        # TODO: Guard against out of bounds assignments
        row_offset = (self._rows - len(lines)) // 2

        for line_num, line in enumerate(lines):
            col_offset = (self._cols - len(line.value)) // 2
            target_row = row_offset + line_num
            for char_num, char in enumerate(line.value):
                target_col = col_offset + char_num
                self._board[target_row][target_col] = Text(char, line.type)
