class BoardView:
    def __init__(self, board_contents, my_value, empty_value):
        self.board = list(map(lambda row: map(lambda v: 1 if v == my_value else 0 if v == empty_value else -1, row), board_contents))

    def __str__(self):
        return '\n'.join(map(lambda r : ' '.join(map(str,r)), reversed(self.board)))
