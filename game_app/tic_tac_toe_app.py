from typing import Dict
import uuid
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class TicTacToeApp:
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}

    def generate_id(self):
        #return_id = str(uuid.uuid4())
        return str(uuid.uuid4())
        #firs_id = "000000000000000000000000000000000000"
        #return_id = str(firs_id[0:-(len(str(len(self._games)+1)))] + str(len(self._games)))
        #return return_id

    def remove_game(self, game_id: str):
        if game_id in self._games:
            del self._games[game_id]
            return True
        else:
            return False

    def can_create_game(self, first_player_id: str, second_player_id: str):
        if (first_player_id.lower()  == "draw" or second_player_id.lower() == "draw") or (first_player_id == second_player_id):
            return False
        else:
            return True

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        id = self.generate_id()
        self._games[id] = TicTacToeGame(
            game_id= id,
            first_player_id= first_player_id,
            second_player_id= second_player_id
        )
        return self._games.get(id).get_game_info()


    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        return self._games.get(game_id).get_game_info()

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        return self._games.get(game_id).do_turn(turn)

    def games_count(self):
        return len(self._games)
    
    def whoisturn(self, game_id):
        return self._games.get(game_id).current_player_id()