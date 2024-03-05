from dataclasses import dataclass

from ..enumerations.text_type import TextType


@dataclass
class Text:
    value: str
    type: TextType = TextType.DEFAULT
