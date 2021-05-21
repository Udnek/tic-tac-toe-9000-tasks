from flask import Flask, request, abort, redirect, url_for

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from game_app import TicTacToeApp
from game_engine import TicTacToeGameInfo, TicTacToeTurn

@dataclass_json
@dataclass
class Person:
    name: str
    age: int

app = Flask(__name__)
game_app = TicTacToeApp()

@app.route('/')
def index():
    return f'TicTacToe1996. Games now: {game_app.games_count()}. Command do start: /start/first_player/second_player'
    #return redirect(url_for('login'))

@app.route('/start/<fir>/<sec>')
def start(fir,sec):
    if game_app.can_create_game(fir, sec):
        gameid = game_app.start_game(fir,sec).game_id
        #return redirect(url_for(f'{gameid}'))
        return f'Game created! {fir} vs {sec}! Game ID: {gameid}. Command to turn: /turn/{gameid}/{game_app.whoisturn(gameid)}/x/y'
    else:
        return f'Can`t create game! Incrorrect values'

@app.route('/turn/<gameid>/<name>/<x>/<y>')
def turn(gameid,name,x,y):
    game_app.do_turn(TicTacToeTurn(name, int(x), int(y)), gameid)
    game = game_app.get_game_by_id(gameid)
    if game.winner_id == "": 
        return f'Game ID: {gameid}. Turn: {name}, X:{x}, Y:{y}. Game: {game.field}. Command to turn: /turn/{gameid}/{game_app.whoisturn(gameid)}/x/y' 
    elif game.winner_id == "Draw":
        return f'Game ID: {gameid}. Turn: {name}, X:{x}, Y:{y}. Game: {game.field}. {game.winner_id} WIN! Game END.'
    else:
        return f'Game ID: {gameid}. Turn: {name}, X:{x}, Y:{y}. Game: {game.field}. DRAW! Game END!'

@app.route('/remove/<gameid>')
def remove(gameid):
    if game_app.remove_game(gameid):
        return f'Game successfully remove! Game ID: {gameid}'
    else:
        return f'Game ID: {gameid} not found!'