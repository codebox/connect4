from board_view import BoardView
from board import Board

class Game:
    DRAW_REWARD = 0
    WIN_REWARD = 1
    LOSE_REWARD = -1

    def __init__(self, board, players):
        self.players = players
        self.board = board
        self.move_counter = 0
        self.finished = False
        self.winner = None

    def move(self):
        if len(self.board.get_valid_moves()) == 0:
            self.finished = True
            for player in self.players:
                player.update_with_result(Game.DRAW_REWARD)

            return

        self.move_counter += 1
        player = self.players[(self.move_counter - 1) % len(self.players)]
        board_view = BoardView(self.board.board, player.id, Board.EMPTY_CELL)
        move = player.move(board_view)
        lines = self.board.drop(move, player.id)

        print('Player {} plays {}'.format(player.id, move))

        if len(lines) > 0:
            self.finished = True
            self.winner = player.id
            for p in self.players:
                p.update_with_result(Game.WIN_REWARD if p.id == self.winner else Game.LOSE_REWARD)
