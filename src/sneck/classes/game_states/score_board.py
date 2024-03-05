from ...enumerations.text_type import TextType
from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext
from ...tools import painter
from ..text import Text


class ScoreBoardState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game = state_manager.game

        self.editing = False
        self._rank = self.game.score_board_data.get_rank(self.game.score)

        if self._rank:
            self._entry = self.game.score_board_data.insert_entry(self.game.score)
            self.editing = True

        self.game.screen.palette.load_default_theme()
        self.game.screen.disable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        self._make_score_text()

        self.game.screen.add_board(self.game.board)
        self.game.screen.refresh()

        while self.state_manager.state == self:
            if self.editing:
                self._process_name_entry()
            else:
                self._process_user_input()

    def _make_score_text(self) -> None:
        lines: list[Text] = [Text("H I G H  S C O R E S", TextType.HIGH_SCORE_TITLE), Text("")]
        spacing = " " * 2

        for index, entry in enumerate(self.game.score_board_data.entries):
            rank = index + 1
            player_text = entry.player or ""
            points_text = f"{entry.score:04d}"

            score_text = Text(
                f"{str(rank).rjust(2, " ")}.{spacing}{points_text}{spacing}{player_text.ljust(3, " ")}\n", TextType.HIGH_SCORE_TEXT
            )

            lines.append(score_text)
            lines.append(Text(""))

        lines.pop(-1)
        painter.paint_centre_text(self.game.board, lines)

    def _process_user_input(self):
        key = self.game.screen.get_key().upper()

        if key == " ":
            self.state_manager.transition_to_title_screen()

    def _process_name_entry(self):
        key = self.game.screen.get_key().upper()

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
            self.game.score_board_data.save()

        self._make_score_text()
        self.game.screen.add_board(self.game.board)
        self.game.screen.refresh()
