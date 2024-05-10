from dataclasses import dataclass

from sneck.classes.board import Board
from sneck.classes.text import Text


@dataclass
class Output:
    board: Board
    score_bar_text: Text
