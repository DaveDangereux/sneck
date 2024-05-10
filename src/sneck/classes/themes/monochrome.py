from sneck.enumerations import Colour

from .default import DefaultTheme


class MonochromeTheme(DefaultTheme):
    SNAKE = Colour.WHITE
    WALL = Colour.WHITE
    FRUIT = Colour.WHITE
    SCORE_BAR = Colour.WHITE
