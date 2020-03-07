from game import Game
from player import Player
from board import Board
from random import shuffle


class Tournament:
    def __init__(self, game_count, players):
        self.game_count = game_count
        self.players = players

    def run(self, save_on_finish=True, update_handler=None):
        game_number = 1
        wins = {None:0}
        recent_wins = {None:0}
        for player in self.players:
            wins[player.id] = 0
            recent_wins[player.id] = 0

        while game_number <= self.game_count:
            board = Board()
            shuffle(self.players)
            game = Game(board, self.players, game_number)
            while not game.finished:
                player = game.get_next_player()
                move = player.strategy.move(game, player.id)
                game.move(move, player.id)

            print(game.winner or '-', end='', flush=True)
            wins[game.winner] += 1
            recent_wins[game.winner] += 1
            for player in self.players:
                reward = 1 if player.id == game.winner else 0 if game.winner is None else -1
                player.strategy.game_over(reward)

            game_number += 1
            if game_number % 5 == 0:
                if update_handler:
                    update_handler(recent_wins)
                recent_wins[None] = 0
                for player in self.players:
                    recent_wins[player.id] = 0

        if save_on_finish:
            self.close()

        return wins

    def close(self):
        [p.strategy.save() for p in self.players]