import curses

from sneck.classes.output import Output
from sneck.classes.palette import Palette


class Display:
    def __init__(self):

        # curses aliases
        self._stdscr = curses.initscr()
        self._add_char = self._stdscr.addch
        self._add_string = self._stdscr.addstr
        self._erase = self._stdscr.erase
        self._refresh = self._stdscr.refresh

        self.stop = curses.endwin

        # Screen dimensions
        self._rows, self._columns = self._stdscr.getmaxyx()

        # Initialise colour
        self.palette = Palette()
        self._stdscr.bkgd(" ", self.palette.WHITE)

    def load_default_theme(self):
        self.palette.load_default_theme()

    def next_theme(self):
        self.palette.next_theme()

    def display_output(self, output: Output):
        self._erase()

        board_height = output.board.get_height()
        board_start_row = (self._rows - board_height) // 2
        board_start_column = (self._columns - output.board.get_width()) // 2

        # Display board
        for row_index, row in enumerate(output.board.get_lines()):
            for col_index, text in enumerate(row):
                self._add_char(
                    row_index + board_start_row,
                    col_index + board_start_column,
                    text.value,
                    self.palette.get_colour_from_type(text.type),
                )

        # Draw score bar
        self._add_string(
            board_start_row - 1,
            board_start_column,
            output.score_bar_text.value,
            self.palette.get_colour_from_type(output.score_bar_text.type),
        )

        self._refresh()
