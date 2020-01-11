import random


class RandomStrategy:
    def __init__(self):
        pass

    def move(self, game, player_id):
        return random.choice(game.board.get_valid_moves())

    def update(self, player_id, winner):
        pass