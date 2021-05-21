from copy import deepcopy
from typing import Callable, List, Optional
from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    """Наследуемся от абстрактного класса и реализуем ручками все методы"""

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns: List[TicTacToeTurn] = []
        #self.__current_player_id = ""

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        x = turn.x_coordinate
        y = turn.y_coordinate
        whatreturn = False
        if (0 <= x <= 2) and (0 <= y <= 2) and (self.get_game_info().field[x][y] == " ") and (self.__winner_id == "") and (self.current_player_id() == turn.player_id):
            whatreturn = True
        return whatreturn

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) == True:
            self.__turns.append(turn)
            self.__winner_id = self.win(self.get_game_info().field, True)
        return self.get_game_info()

    def win(self, field, checkturns):
        if (checkturns) and (len(self.__turns) == 8):
            print(field)
            for i in range(3):
                for j in range(3):
                    if field[i][j] == " ":
                        cords = [i,j]

            field2 = field[:]
            if self.current_player_id() == self.__first_player_id:
                field2[cords[0]][cords[1]] = "X"
            else:
                field2[cords[0]][cords[1]] = "O"

            winnerpred = self.win(field2, False)
            if winnerpred == self.__first_player_id:
                self.winner_id = self.__first_player_id
                return self.__first_player_id
            elif winnerpred == self.__second_player_id:
                self.winner_id = self.__second_player_id
                return self.__second_player_id
            else:
                self.winner_id = "Draw"
                return "Draw"

        xo = ["X", "O"]
        whoiswin = ""
       #horizontale
        for sym in xo:
            for i in range(3):
                combo = 0
                for j in range(3):
                    if field[i][j] == sym:
                        combo += 1
                if combo == 3:
                    if sym == "X":
                        whoiswin = self.__first_player_id
                    else:
                        whoiswin = self.__second_player_id
        #verticale"""
        for sym in xo:
            for i in range(3):
                combo = 0
                for j in range(3):
                    if field[j][i] == sym:
                        combo += 1
                if combo == 3:
                    if sym == "X":
                        whoiswin = self.__first_player_id
                    else:
                        whoiswin = self.__second_player_id
        #from left up to right down"""
        for sym in xo:
            if (field[0][0]==sym)and(field[1][1]==sym)and(field[2][2]==sym):
                if sym == "X":
                    whoiswin = self.__first_player_id
                else:
                    whoiswin = self.__second_player_id
        #from right up to left down"""
        for sym in xo:
            if (field[0][2] == sym)and(field[1][1] == sym)and(field[2][0] == sym):
                if sym == "X":
                    whoiswin = self.__first_player_id
                else:
                    whoiswin = self.__second_player_id
        
        if (len(self.__turns) == 9) and whoiswin == "":
            whoiswin = "Draw"
            return whoiswin
        self.__winner_id = whoiswin
        return whoiswin

    def current_player_id(self):
        if (self.__turns == []) or (len(self.__turns)%2 == 0):
            #self.__current_player_id = self.__first_player_id
            return self.__first_player_id
        else:
            if len(self.__turns) % 2 == 0:
                #self.__current_player_id = self.__first_player_id
                return self.__first_player_id
            else:
                #self.__current_player_id = self.__second_player_id
                return self.__second_player_id



    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if  turn.player_id == self.__first_player_id:
                ch = "X"      
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result
        