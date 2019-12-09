import random

class RandomStrategy:
    def __init__(self):
        pass

    def move(self, board_view):
        available_moves = [i for i, v in enumerate(board_view.board[-1]) if v == 0]
        return random.choice(available_moves)

    def update(self, result):
    	pass