from dataclasses import dataclass

from sneck.enumerations import TextType


@dataclass
class Text:
    value: str
    type: TextType = TextType.DEFAULT

    def clear(self):
        self.value = ""
