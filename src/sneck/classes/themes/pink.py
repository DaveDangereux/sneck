from ...enumerations.colour import Colour
from .default import DefaultTheme


class PinkTheme(DefaultTheme):
    SNAKE = Colour.WHITE
    WALL = Colour.MAGENTA
    FRUIT = Colour.WHITE
    SCORE = Colour.WHITE
