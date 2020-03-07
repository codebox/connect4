from board import Board
from random import random, choice
from strategy import Strategy

def no_exploration(g):
    return 0

class NnStrategy(Strategy):

    def __init__(self, network, get_exploration_factor=no_exploration):
        self.discount_factor = 0.9
        self.get_exploration_factor = get_exploration_factor
        self.current_game_moves = []
        self.network = network
        self.current_batch_board_states = []
        self.current_batch_rewards = []
        self.batch_size = 100

    def move(self, game, player_id):
        move_scores = {}

        valid_moves = game.board.get_valid_moves()

        if random() < self.get_exploration_factor(game.game_number):
            move_to_play = choice(valid_moves)

            game_copy = game.clone()
            game_copy.move(move_to_play, player_id)
            board_state = self._build_board_state(game_copy, player_id)

        else:
            for move in valid_moves:
                game_copy = game.clone()
                game_copy.move(move, player_id)
                board_state = self._build_board_state(game_copy, player_id)
                score = self.network.eval_position(board_state)
                move_scores[move] = (score, board_state)

            move_to_play = max(move_scores.keys(), key=lambda k: move_scores.get(k)[0])
            board_state = move_scores[move_to_play][1]

        self.current_game_moves.append((board_state, move_to_play))

        return move_to_play

    def game_over(self, reward):
        for board_state, move in reversed(self.current_game_moves):
            self.current_batch_board_states.append(board_state)
            self.current_batch_rewards.append(reward)
            reward *= self.discount_factor

        if len(self.current_batch_rewards) >= self.batch_size:
            self.network.update(self.current_batch_board_states, self.current_batch_rewards)
            self.current_batch_board_states = []
            self.current_batch_rewards = []

        self.current_game_moves = []

    def save(self):
        self.network.save()

    def get_name(self):
        return self.network.get_name()

    def _build_board_state(self, game, player_id):
        bs = list(map(lambda row: list(map(lambda v: 1 if v == player_id else 0 if v == Board.EMPTY_CELL else -1, row)), game.board.board))

        return bs
