from game import Game
from player import Player
from board import Board


class Tournament:
    def __init__(self, game_count, strategies):
        self.game_count = game_count
        self.players = list(map(lambda t: Player(chr(65 + t[0]), t[1]), enumerate(strategies)))

    def run(self):
        game_number = 1
        wins = {}
        while game_number <= self.game_count:
            board = Board()
            game = Game(board, self.players)
            while not game.finished:
                player = game.get_next_player()
                move = player.strategy.move(game, player.id)
                game.move(move, player.id)
            if game.winner not in wins:
                wins[game.winner] = 0
            wins[game.winner] += 1
            for player in self.players:
                player.strategy.update(player.id, game.winner)
            # print(str(game.winner) + ' wins game ' + str(game_number))
            # print(board)
            game_number += 1

        print('tournament finished')
        print(wins)
