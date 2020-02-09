import random
from strategy import Strategy


class RandomStrategy(Strategy):
    def move(self, game, player_id):
        return random.choice(game.board.get_valid_moves())

    def game_over(self, reward):
        pass

    def save(self):
        pass

    def get_name(self):
        return 'RND'
