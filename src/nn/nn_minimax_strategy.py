from board import Board
from strategy import Strategy
import math, time

class NnMiniMaxStrategy(Strategy):

    def __init__(self, network, lookahead_limit, player_ids):
        self.network = network
        self.lookahead_limit = lookahead_limit
        self.player_ids = player_ids
        self.total_time = 0
        self.total_moves = 0

    def move(self, game, player_id):
        def fn_eval(game):
            return self._value_with_lookahead(game, player_id, self.lookahead_limit)

        t0 = time.time()
        move = self._find_best_move_and_score_for_player(game, player_id, fn_eval)[0]
        self.total_time += time.time() - t0
        self.total_moves += 1
        return move

    def average_move_time(self):
        return self.total_time / self.total_moves

    def _value_with_lookahead(self, game, player_id, lookaheads_remaining):
        if lookaheads_remaining == 0:
            board_state = self._build_board_state(game, player_id)
            score = self.network.eval_position(board_state)
        else:
            other_player_id = self._get_other_player(player_id)
            def fn_eval(game):
                return self._value_with_lookahead(game, other_player_id, lookaheads_remaining-1)
            score = -self._find_best_move_and_score_for_player(game, other_player_id, fn_eval)[1]

        return score

    def _find_best_move_and_score_for_player(self, game, player_id, fn_eval):
        valid_moves = game.board.get_valid_moves()
        move_scores = {}
        for move in valid_moves:
            game_copy = game.clone()
            game_copy.move(move, player_id)
            if game_copy.finished:
                move_scores[move] = math.inf if game_copy.winner == player_id else 0 if not game_copy.winner else -math.inf
            else:
                move_scores[move] = fn_eval(game_copy)

        best_move = max(list(move_scores.keys()), key=lambda k: move_scores.get(k))
        return best_move, move_scores[best_move]

    def _get_other_player(self, player_id):
        return next(p for p in self.player_ids if p != player_id)

    def game_over(self, reward):
        pass

    def save(self):
        pass

    def get_name(self):
        return self.network.get_name() + 'mm'

    def _build_board_state(self, game, player_id):
        bs = list([list([1 if v == player_id else 0 if v == Board.EMPTY_CELL else -1 for v in row]) for row in game.board.board])

        return bs
