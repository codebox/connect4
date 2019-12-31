class Player:
    def __init__(self, id, strategy=None):
        self.id = id
        self.strategy = strategy

    def move(self, game):
        return self.strategy.move(game, self.id)
