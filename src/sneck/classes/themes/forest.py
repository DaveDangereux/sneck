from ...enumerations.colour import Colour
from .default import DefaultTheme


class ForestTheme(DefaultTheme):
    SNAKE = Colour.GREEN
    WALL = Colour.GREEN
    FRUIT = Colour.RED
    SCORE = Colour.GREEN
