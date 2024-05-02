from ...enumerations.colour import Colour
from ...protocols.theme import Theme


class DefaultTheme(Theme):
    DEFAULT = Colour.WHITE
    SNAKE = Colour.GREEN
    WALL = Colour.WHITE
    FRUIT = Colour.RED
    SCORE = Colour.WHITE
    TITLE = Colour.GREEN
    INFO = Colour.WHITE
    GAME_OVER = Colour.RED
    HIGH_SCORE_TITLE = Colour.RED
    HIGH_SCORE_TEXT = Colour.WHITE
    HIGH_SCORE_TEXT_ACTIVE = Colour.RED
