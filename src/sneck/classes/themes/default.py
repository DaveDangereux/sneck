from ...enumerations.colour import Colour
from ...protocols.theme import Theme


class DefaultTheme(Theme):
    DEFAULT = Colour.WHITE
    SNAKE = Colour.GREEN
    WALL = Colour.MAGENTA
    FRUIT = Colour.RED
    SCORE = Colour.YELLOW
    TITLE = Colour.GREEN
    INFO = Colour.WHITE
    GAME_OVER = Colour.RED
    HIGH_SCORES = Colour.MAGENTA
