from ...enumerations.colour import Colour
from .default import DefaultTheme


class MonochromeTheme(DefaultTheme):
    SNAKE = Colour.WHITE
    WALL = Colour.WHITE
    FRUIT = Colour.BLUE
    SCORE = Colour.WHITE
