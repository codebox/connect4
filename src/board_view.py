class BoardView:
    def __init__(self, board_contents, my_value, empty_value):
        self.board = list(map(lambda row: map(lambda v: 1 if v == my_value else 0 if v == empty_value else -1, row), board_contents))

    def to_id(self):
        return ' '.join(map(lambda r : ''.join(map(self.__transform_value_for_displau,r)), reversed(self.board)))

    def __str__(self):
        return '\n'.join(map(lambda r : ' '.join(map(self.__transform_value_for_displau,r)), reversed(self.board)))

    def __transform_value_for_displau(self, value):
        return 'X' if value == 1 else 'o' if value == -1 else '.'
