from ..assets.ascii_chars import box_chars
from ..classes.board import Board
from ..classes.text import Text


def paint_border(board: Board) -> None:
    for row in board:
        row[0] = box_chars["vertical_bar"]
        row[-1] = box_chars["vertical_bar"]

    board[0] = [box_chars["horizontal_bar"] for _ in board[0]]
    board[0][0] = box_chars["top_left"]
    board[0][-1] = box_chars["top_right"]

    board[-1] = [box_chars["horizontal_bar"] for _ in board[0]]
    board[-1][0] = box_chars["bottom_left"]
    board[-1][-1] = box_chars["bottom_right"]


def paint_centre_text(board: Board, lines: list[Text]) -> None:
    # TODO: Guard against out of bounds assignments
    rows, cols = board.get_dimensions()
    row_offset = (rows - len(lines)) // 2

    for line_num, line in enumerate(lines):
        col_offset = (cols - len(line.value)) // 2
        target_row = row_offset + line_num
        for char_num, char in enumerate(line.value):
            target_col = col_offset + char_num
            board[target_row][target_col] = Text(char, line.type)
