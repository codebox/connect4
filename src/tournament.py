from game import Game
from player import Player
from board import Board
from random import shuffle

class Tournament:
    def __init__(self, game_count, players):
        self.game_count = game_count
        # self.players = list(map(lambda t: Player(chr(65 + t[0]), t[1]), enumerate(strategies)))
        self.players = players

    def run(self):
        game_number = 1
        wins = {None:0}
        recent_wins = {None:0}
        for player in self.players:
            wins[player.id] = 0
            recent_wins[player.id] = 0

        while game_number <= self.game_count:
            board = Board()
            shuffle(self.players)
            game = Game(board, self.players)
            while not game.finished:
                player = game.get_next_player()
                move = player.strategy.move(game, player.id)
                game.move(move, player.id)

            wins[game.winner] += 1
            recent_wins[game.winner] += 1
            for player in self.players:
                player.strategy.update(player.id, game.winner)

            game_number += 1
            if game_number % 100 == 0:
                print(recent_wins)
                recent_wins[None] = 0
                for player in self.players:
                    recent_wins[player.id] = 0


        print('tournament finished')
        print(wins)
        self.close()

    def close(self):
        [p.strategy.on_end() for p in self.players]