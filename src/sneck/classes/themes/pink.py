from sneck.enumerations import Colour

from .default import DefaultTheme


class PinkTheme(DefaultTheme):
    SNAKE = Colour.BLUE
    WALL = Colour.MAGENTA
    FRUIT = Colour.RED
    SCORE_BAR = Colour.MAGENTA
