class Player:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
        self.score = 0

    def move(self, game):
        return self.strategy.move(game, self.id)
