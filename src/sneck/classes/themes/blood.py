from ...enumerations.colour import Colour
from .default import DefaultTheme


class BloodTheme(DefaultTheme):
    SNAKE = Colour.RED
    WALL = Colour.RED
    FRUIT = Colour.GREEN
    SCORE = Colour.RED
