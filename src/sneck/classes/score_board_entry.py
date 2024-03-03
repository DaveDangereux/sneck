from dataclasses import dataclass


@dataclass
class ScoreBoardEntry:
    player: str
    points: int
