from enum import Enum


class GameState(Enum):
    TITLE_SCREEN = "TITLE_SCREEN",
    GAME_LOOP = "PLAY",
    GAME_OVER = "GAME_OVER"
