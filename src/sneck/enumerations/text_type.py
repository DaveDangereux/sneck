from enum import Enum


class TextType(Enum):
    DEFAULT = "DEFAULT"
    SNAKE = "SNAKE"
    WALL = "WALL"
    FRUIT = "FRUIT"
    SCORE = "SCORE"
    TITLE = "TITLE"
    INFO = "INFO"
    GAME_OVER = "GAME_OVER"
    HIGH_SCORES = "HIGH_SCORES"
