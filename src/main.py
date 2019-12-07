from board import Board
from player import Player
from game import Game
from random_strategy import RandomStrategy

board = Board(7, 6, 4)
players = [Player('X', RandomStrategy()), Player('O', RandomStrategy())]
game = Game(board, players)

while not game.finished:
    game.move()

if game.winner:
    print('Player {} wins'.format(game.winner))
else:
    print('Draw')

print(board)