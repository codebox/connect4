from tournament import Tournament
from board import Board
from random_strategy import RandomStrategy

board = Board(7, 6, 4)
strategies = [RandomStrategy(), RandomStrategy()]

tournament = Tournament(board, 10, strategies)
tournament.run()