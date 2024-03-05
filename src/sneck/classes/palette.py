import curses

from ..enumerations.colour import Colour
from ..enumerations.text_type import TextType
from .themes.blood import BloodTheme
from .themes.custard import CustardTheme
from .themes.default import DefaultTheme
from .themes.forest import ForestTheme
from .themes.monochrome import MonochromeTheme
from .themes.pink import PinkTheme
from .themes.space import SpaceTheme


class Palette:
    themes = [
        DefaultTheme,
        CustardTheme,
        ForestTheme,
        SpaceTheme,
        BloodTheme,
        MonochromeTheme,
        PinkTheme,
    ]

    def __init__(self):
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

        self.theme = self.load_default_theme()

        for colour in Colour:
            if colour.name not in dir(self):
                raise AttributeError(
                    f"{colour.name} not implemented in {self.__class__.__name__}"
                )

    def get_colour_from_type(self, text_type: TextType) -> int:
        colour = getattr(self.theme, text_type.name)
        return getattr(self, colour.name)

    def load_default_theme(self):
        self.theme = DefaultTheme

    def load_next_theme(self):
        current_theme_index = self.themes.index(self.theme)
        next_theme_index = (current_theme_index + 1) % len(self.themes)
        self.theme = self.themes[next_theme_index]
