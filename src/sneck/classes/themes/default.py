from sneck.classes.theme import Theme
from sneck.enumerations import Colour


class DefaultTheme(Theme):
    DEFAULT = Colour.WHITE
    SNAKE = Colour.GREEN
    WALL = Colour.WHITE
    FRUIT = Colour.RED
    FINAL_SCORE = Colour.WHITE
    SCORE_BAR = Colour.WHITE
    TITLE = Colour.GREEN
    INFO = Colour.YELLOW
    GAME_OVER = Colour.RED
    HIGH_SCORE_TITLE = Colour.RED
    HIGH_SCORE_TEXT = Colour.WHITE
    HIGH_SCORE_TEXT_ACTIVE = Colour.RED
