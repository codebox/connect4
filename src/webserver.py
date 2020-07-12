#!/usr/bin/python

from bottle import route, run, abort, request, response, error, static_file
from json import dumps
import re
from board import Board
from game import Game
from player import Player
from mcts.mcts_strategy import MctsStrategy
from nn.nn_strategy import NnStrategy
from nn.network_64x2_64x2_64_64 import NetworkA
from nn.network_128x4_64_64 import NetworkB
from nn.network_64x4_64x2_64x2_64 import NetworkD

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


@route('/<filename:re:.*>')
def server_static(filename):
    return static_file(filename, root='../web')

@route('/connect4', method='POST')
def move():
    requestJson = request.json
    rows = requestJson['board']
    iter = requestJson['iters']

    if iter > MAX_ITERS:
        abort(400, 'iter value too high, max ' + str(MAX_ITERS))

    if len(rows) != Board.ROW_COUNT:
        abort(400, 'bad request format')

    if not all(ROW_PATTERN.match(row) for row in rows):
        abort(400, 'bad values in row')

    board = Board()
    winner = populate_board(board, [list(row) for row in rows])
    move = None

    if not winner:
        players = [Player('0'), Player('1')]
        game = Game(board, players)
        # strategy = MctsStrategy()
        # strategy.rollout_limit = iter
        # strategy = NnStrategy(NetworkA(), False)
        strategy = NnStrategy(NetworkD())

        move = strategy.move(game, '0')
        lines = board.drop(move, '0');
        winner = '0' if len(lines) else None

    response.content_type = 'application/json'

    return dumps({
        "move" : move,
        "winner" : winner
    })

def populate_board(board, rows):
    for row in reversed(rows):
        for col, value in enumerate(row):
            if value != Board.EMPTY_CELL:
                lines = board.drop(col, value)
                if len(lines):
                    return value


run(host='localhost', port=8080, debug=True)
