import curses

from sneck.classes.board import Board
from sneck.classes.palette import Palette
from sneck.classes.text import Text


class Screen:
    def __init__(self, board_rows: int, board_cols: int):
        self._stdscr = curses.initscr()

        # Expose curses / stdscr methods
        self.add_char = self._stdscr.addch
        self.add_string = self._stdscr.addstr
        self.erase = self._stdscr.erase
        self.get_key = self._stdscr.getkey
        self.refresh = self._stdscr.refresh
        self.stop = curses.endwin
        self._rows, self._cols = self._stdscr.getmaxyx()

        self._board_row_offset = (self._rows - board_rows) // 2
        self._board_col_offset = (self._cols - board_cols) // 2

        # Basic init
        curses.noecho()
        curses.curs_set(0)
        self._stdscr.nodelay(True)

        # Initialise colour
        self.palette = Palette()
        self._stdscr.bkgd(" ", self.palette.WHITE)

    def disable_animation(self) -> None:
        self._stdscr.nodelay(False)

    def enable_animation(self) -> None:
        self._stdscr.nodelay(True)

    def add_board(self, board: Board) -> None:
        for row_index, row in enumerate(board.get_lines()):
            for col_index, text in enumerate(row):
                self.add_char(
                    row_index + self._board_row_offset,
                    col_index + self._board_col_offset,
                    text.value,
                    self.palette.get_colour_from_type(text.type),
                )

    def add_score_bar(self, score_bar_text: Text) -> None:
        self.add_string(
            self._board_row_offset - 1,
            self._board_col_offset,
            score_bar_text.value,
            self.palette.get_colour_from_type(score_bar_text.type),
        )

    def add_debug_info(self, board: Board, text: str) -> None:
        board_rows, _ = board.get_dimensions()
        row_offset = (self._rows - board_rows) // 2 + board_rows

        self.add_string(row_offset, 40, text)

    def _right_justify_text(self, text: str, width: int) -> str:
        left_space = " " * (width - len(text))
        return left_space + text
