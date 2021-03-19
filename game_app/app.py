from typing import Dict

from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class TicTacToeApp:
    def __init__(self):
        """пока не знаю, мб что-то ещё тут будет :)
        в обоих случаях айдишник - ключ, значение - угадайте-, что)"""
        self._games: Dict[str, TicTacToeGame] = {}
        self._id = str(len(self._games))

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        self._games[self._id] = TicTacToeGame(
            game_id=self._id,
            first_player_id= first_player_id,
            second_player_id= second_player_id
        )

    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:
        return self._games.get(game_id).get_game_info

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        return self._games.get(game_id).do_turn(turn)