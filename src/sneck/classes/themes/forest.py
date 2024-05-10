from sneck.enumerations import Colour

from .default import DefaultTheme


class ForestTheme(DefaultTheme):
    SNAKE = Colour.GREEN
    WALL = Colour.GREEN
    FRUIT = Colour.RED
    SCORE_BAR = Colour.GREEN
