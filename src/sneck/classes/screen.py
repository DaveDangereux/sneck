import curses

from ..assets.ascii_chars import box_chars, fruit, snake_chars
from .board import Board


class Screen:
    def __init__(self):
        self._stdscr = curses.initscr()

        # Expose curses / stdscr methods
        self.add_char = self._stdscr.addch
        self.add_string = self._stdscr.addstr
        self.erase = self._stdscr.erase
        self.get_key = self._stdscr.getkey
        self.refresh = self._stdscr.refresh
        self.stop = curses.endwin
        self._rows, self._cols = self._stdscr.getmaxyx()

        # Basic init
        curses.noecho()
        curses.curs_set(0)
        self._stdscr.nodelay(True)

        # Initialise colour
        curses.start_color()

        curses.init_pair(1, curses.COLOR_WHITE, 16)
        curses.init_pair(2, curses.COLOR_RED, 16)
        curses.init_pair(3, curses.COLOR_YELLOW, 16)
        curses.init_pair(4, curses.COLOR_GREEN, 16)
        curses.init_pair(5, curses.COLOR_CYAN, 16)
        curses.init_pair(6, curses.COLOR_BLUE, 16)
        curses.init_pair(7, curses.COLOR_MAGENTA, 16)

        self.WHITE = curses.color_pair(1)
        self.RED = curses.color_pair(2)
        self.YELLOW = curses.color_pair(3)
        self.GREEN = curses.color_pair(4)
        self.CYAN = curses.color_pair(5)
        self.BLUE = curses.color_pair(6)
        self.MAGENTA = curses.color_pair(7)

        self._stdscr.bkgd(" ", self.WHITE)

    def disable_animation(self) -> None:
        self._stdscr.nodelay(False)

    def enable_animation(self) -> None:
        self._stdscr.nodelay(True)

    def add_board(self, board: Board) -> None:
        # TODO: Protect against exceptions due to the terminal being too small
        # to draw the full string
        board_rows, board_cols = board.get_dimensions()
        col_offset = (self._cols - board_cols) // 2
        row_offset = (self._rows - board_rows) // 2

        for row_index, row in enumerate(board.get_lines()):
            for char_index, char in enumerate(row):
                colour = self.WHITE

                if char in box_chars.values():
                    colour = self.MAGENTA
                elif char in snake_chars.values():
                    colour = self.GREEN
                elif char is fruit:
                    colour = self.RED

                self.add_char(
                    row_index + row_offset, char_index + col_offset, char, colour
                )

    def add_score(self, board: Board, score: int) -> None:
        score_text = f"Score: {score:03d}"
        formatted_score_text = (
            self._right_justify_text(score_text, board.get_width()) + "\n"
        )

        board_rows, board_cols = board.get_dimensions()
        col_offset = (self._cols - board_cols) // 2
        row_offset = (self._rows - board_rows) // 2 - 1

        self.add_string(row_offset, col_offset, formatted_score_text, self.YELLOW)

    def add_debug_info(self, board: Board, text: str) -> None:
        board_rows, _ = board.get_dimensions()
        row_offset = (self._rows - board_rows) // 2 + board_rows

        self.add_string(row_offset, 40, text)

    def _right_justify_text(self, text: str, width: int) -> str:
        left_space = " " * (width - len(text))
        return left_space + text
