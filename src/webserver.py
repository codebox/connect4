#!/usr/bin/python

from bottle import route, run, abort, request, response, error
from json import dumps
import re
from board import Board
from game import Game
from player import Player
from mcts.mcts_strategy import MctsStrategy

ROW_PATTERN = re.compile(r"^[\.01]{" + str(Board.COLUMN_COUNT) + "}")
MAX_ITERS = 10000


@error(400)
@error(500)
def json_error(error):
    print(error)
    error_data = {
        'error': error.body
    }
    response.content_type = 'application/json'
    return dumps(error_data)


@route('/connect4', method='POST')
def move():
    json = request.json
    rows = json['board']
    iter = json['iters']

    if iter > MAX_ITERS:
        abort(400, 'iter value too high, max ' + str(MAX_ITERS))

    if len(rows) != Board.ROW_COUNT:
        abort(400, 'bad request format')

    if not all(ROW_PATTERN.match(row) for row in rows):
        abort(400, 'bad values in row')

    board = Board()
    populate_board(board, [list(row) for row in rows])

    players = [Player('0'), Player('1')]
    game = Game(board, players)
    strategy = MctsStrategy()
    strategy.rollout_limit = iter

    move = strategy.move(game, '1')

    response.content_type = 'application/json'

    return str(move)

def populate_board(board, rows):
    for row in reversed(rows):
        for col, value in enumerate(row):
            if value != Board.EMPTY_CELL:
                lines = board.drop(col, value)
                if len(lines):
                    abort(400, 'game already complete')


run(host='localhost', port=8080, debug=True)
