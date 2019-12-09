from game import Game
from player import Player

class Tournament:

    def __init__(self, board, game_count, strategies):
        self.board = board
        self.game_count = game_count
        self.players = list(map(lambda t: Player(chr(65 + t[0]), t[1]), enumerate(strategies)))

    def run(self):
        game_number = 1
        while game_number <= self.game_count:
            self.board.reset()
            game = Game(self.board, self.players)
            while not game.finished:
                game.move()
            print(game.winner + ' wins')
            game_number += 1

        print('tournament finished')
        for player in self.players:
            print('{}: {}'.format(player.id, player.score))


