from abc import ABC

from sneck.enumerations import Colour, TextType


class Theme(ABC):
    DEFAULT: Colour
    SNAKE: Colour
    WALL: Colour
    FRUIT: Colour
    FINAL_SCORE: Colour
    SCORE_BAR: Colour
    TITLE: Colour
    INFO: Colour
    GAME_OVER: Colour
    HIGH_SCORE_TITLE: Colour
    HIGH_SCORE_TEXT: Colour
    HIGH_SCORE_TEXT_ACTIVE: Colour

    def __init__(self):
        self._check_theme_protocol_implements_all_text_types()
        self._check_theme_subclass_implements_all_text_types()

    def _check_theme_protocol_implements_all_text_types(self):
        for text_type in TextType:
            if text_type.name not in Theme.__annotations__:
                raise AttributeError(
                    f"{text_type.name} not implemented in {Theme.__name__}"
                )

    def _check_theme_subclass_implements_all_text_types(self):
        for text_type in TextType:
            if text_type.name not in dir(self):
                raise AttributeError(
                    f"{text_type.name} not implemented in {self.__class__.__name__}"
                )
