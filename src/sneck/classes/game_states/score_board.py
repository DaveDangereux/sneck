from sneck.classes.text import Text
from sneck.enumerations import TextType
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class ScoreBoardState(GameState):
    def __init__(self, game: GameContext):
        # game aliases
        self._game = game
        self._board = game.output.board
        self._display = game.display

        self.editing = False
        self._rank = self._game.score_board_data.get_rank(self._game.score)

        self._display.load_default_theme()

        if self._rank:
            self._entry = self._game.score_board_data.insert_entry(self._game.score)
            self.editing = True

    def handle_input(self, key: str):
        if self.editing:
            self._process_name_entry(key)
        elif key == " ":
            self._game.transition_to_title_screen()

    def run(self):
        self._board.clear()
        self._make_score_text()

    def _process_name_entry(self, key: str):
        name_length = len(self._entry.player)

        is_valid_name_char = key.isalnum() or key == " "
        is_backspace = ord(key) == 127
        is_enter = ord(key) == 10

        if is_valid_name_char and name_length < 3:
            self._entry.player += key
        elif is_backspace:
            self._entry.player = self._entry.player[:-1]
        elif is_enter and len(self._entry.player) > 0:
            self.editing = False
            self._game.score_board_data.save()

        self._make_score_text()

    def _make_score_text(self) -> None:
        lines: list[Text] = [
            Text("H I G H  S C O R E S", TextType.HIGH_SCORE_TITLE),
            Text(""),
        ]
        spacing = " " * 2

        for index, entry in enumerate(self._game.score_board_data.entries):
            rank = index + 1
            is_current_player_entry = rank == self._game.score_board_data.get_rank(
                self._game.score
            )
            entry_text_type = (
                TextType.HIGH_SCORE_TEXT_ACTIVE
                if is_current_player_entry
                else TextType.HIGH_SCORE_TEXT
            )
            player_text = entry.player or ""
            points_text = f"{entry.score:04d}"

            score_text = Text(
                f"{str(rank).rjust(2, " ")}.{spacing}{points_text}{spacing}{player_text.ljust(3, " ")}\n",
                entry_text_type,
            )

            lines.append(score_text)
            lines.append(Text(""))

        lines.pop(-1)
        self._board.write_centre_text(lines)
