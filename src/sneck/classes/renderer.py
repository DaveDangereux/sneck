import curses


class Renderer:
    def __init__(self):
        self._stdscr = curses.initscr()

        # Expose curses / stdscr methods
        self.refresh = self._stdscr.refresh
        self.erase = self._stdscr.erase
        self.add_string = self._stdscr.addstr
        self.stop = curses.endwin
        self.get_key = self._stdscr.getkey
        self.add_char = self._stdscr.addch

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
