from ...enumerations.colour import Colour
from .default import DefaultTheme


class SpaceTheme(DefaultTheme):
    SNAKE = Colour.BLUE
    WALL = Colour.BLUE
    FRUIT = Colour.YELLOW
    SCORE = Colour.WHITE
