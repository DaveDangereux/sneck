import curses


class Input:
    def __init__(self):
        self._stdscr = curses.initscr()

        curses.noecho()  # Don't echo input to the screen
        curses.curs_set(0)  # Hide the cursor
        self._stdscr.nodelay(True)  # Don't block while waiting for input

    def get_key(self) -> str:
        try:
            key = self._stdscr.getkey().upper()
        except Exception:
            key = ""

        return key
