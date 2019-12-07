from board_view import BoardView
from board import Board

class Game:
    def __init__(self, board, players):
        self.players = players
        self.board = board
        self.move_counter = 0
        self.finished = False
        self.winner = None

    def move(self):
        if len(self.board.get_valid_moves()) == 0:
            self.finished = True
            print('board full!')

        self.move_counter += 1
        player = self.players[(self.move_counter - 1) % len(self.players)]
        board_view = BoardView(self.board.board, player.id, Board.EMPTY_CELL)
        move = player.move(board_view)
        lines = self.board.drop(move, player.id)

        print('Player {} plays {}'.format(player.id, move))

        if len(lines) > 0:
            print('Player {} wins!'.format(player.id))
            print(self.board)
            self.finished = True
            self.winner = player.id