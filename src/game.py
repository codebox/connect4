class Game:
    def __init__(self, board, players, game_number=0):
        self.players = players
        self.board = board
        self.game_number = game_number
        self.finished = False
        self.winner = None
        self.next_player_index = 0

    def move(self, move, player_id):
        if self.finished:
            raise ValueError('No further moves allowed, game is finished')

        next_player = self.get_next_player()
        if player_id != next_player.id:
            raise ValueError('Bad player_id expected {} but got {}'.format(next_player.id, player_id))

        new_lines = self.board.drop(move, player_id)

        if len(new_lines):
            self.finished = True
            self.winner = player_id

        else:
            self.winner = None
            is_board_full = len(self.board.get_valid_moves()) == 0
            self.finished = is_board_full

        self.next_player_index = (self.next_player_index + 1) % len(self.players)

    def get_next_player(self):
        return self.players[self.next_player_index]

    def clone(self):
        game = Game(self.board.clone(), self.players, self.game_number)
        game.finished = self.finished
        game.winner = self.winner
        game.next_player_index = self.next_player_index
        return game
