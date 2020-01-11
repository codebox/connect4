def load_network():
    pass # TODO

class NnStrategy:
    network = load_network()

    def __init__(self):
        self.discount_factor = 0.9
        self.current_game_moves = []

    def move(self, game):
        move_scores = {}
        for move in game.board.get_valid_moves():
            game_copy = game.clone()
            game_copy.move(move, player_id)
            board_state = self._build_board_state(game_copy, player_id)
            move_scores[move] = NnStrategy.network.eval_position(board_state)

        best_move = max(move_scores.iterkeys(), key=move_scores.get)
        self.current_game_moves.append((board_state, best_move))

        return best_move

    def update(self, player_id, winner):
        reward = 1 if winner == player_id else 0 if winner is None else -1
        for board_state, move in reversed(self.current_game_moves):
            NnStrategy.network.update(board_state, reward)
            reward *= self.discount_factor

        self.current_game_moves = []

    def _build_board_state(self, game, player_id):
        return list(map(lambda row: map(lambda v: 1 if v == player_id else 0 if v == Board.EMPTY_CELL else -1, row), game.board.board))
