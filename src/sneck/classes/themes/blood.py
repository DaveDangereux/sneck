from sneck.enumerations import Colour

from .default import DefaultTheme


class BloodTheme(DefaultTheme):
    SNAKE = Colour.RED
    WALL = Colour.RED
    FRUIT = Colour.WHITE
    SCORE_BAR = Colour.RED
