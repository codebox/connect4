class Player:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy

    def move(self, board_view):
        return self.strategy.move(board_view)