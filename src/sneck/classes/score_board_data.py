import yaml

from .score_board_entry import ScoreBoardEntry


class ScoreBoardData:
    FILENAME = "scores.yaml"
    MAX_NUM_SCORES = 5
    entries: list[ScoreBoardEntry] = []

    def __init__(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = yaml.safe_load(file)
                if data:
                    self.entries = [
                        ScoreBoardEntry(entry["player"] or "", entry["score"] or 0)
                        for entry in data
                    ]
        except FileNotFoundError:
            self.entries = []

        while len(self.entries) < self.MAX_NUM_SCORES:
            self.entries.append(ScoreBoardEntry("AAA", 0))

    def get_rank(self, score: int) -> int:
        for index, entry in enumerate(self.entries):
            if score > entry.score:
                return index + 1
        return 0

    def insert_entry(self, score: int) -> ScoreBoardEntry:
        rank = self.get_rank(score)
        index = rank - 1
        new_entry = ScoreBoardEntry("", score)
        self.entries.insert(index, new_entry)
        while len(self.entries) > self.MAX_NUM_SCORES:
            self.entries.pop(-1)
        return new_entry

    def save(self):
        with open(self.FILENAME, "w") as file:
            yaml.dump([vars(entry) for entry in self.entries], file)
