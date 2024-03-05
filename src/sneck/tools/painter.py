from ..assets.ascii_chars import box_chars
from ..classes.board import Board
from ..classes.score_board_entry import ScoreBoardEntry
from ..classes.text import Text
from ..enumerations.text_type import TextType


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


def paint_scores(board: Board, score_board_entries: list[ScoreBoardEntry]) -> None:
    lines: list[Text] = [Text("H I G H  S C O R E S", TextType.HIGH_SCORES), Text("")]
    spacing = " " * 2

    for index, entry in enumerate(score_board_entries):
        rank = index + 1
        player_text = entry.player or ""
        points_text = f"{entry.score:04d}"

        score_text = Text(
            f"{str(rank).rjust(2, " ")}.{spacing}{points_text}{spacing}{player_text.ljust(3, " ")}", TextType.SCORE
        )

        lines.append(score_text)
        lines.append(Text(""))

    lines.pop(-1)

    paint_centre_text(board, lines)
