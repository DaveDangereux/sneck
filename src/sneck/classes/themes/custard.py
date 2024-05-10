from sneck.enumerations import Colour

from .default import DefaultTheme


class CustardTheme(DefaultTheme):
    SNAKE = Colour.YELLOW
    WALL = Colour.YELLOW
    FRUIT = Colour.MAGENTA
    SCORE_BAR = Colour.YELLOW
