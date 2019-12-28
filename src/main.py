from tournament import Tournament
from random_strategy import RandomStrategy
from mcts.mcts_strategy import MctsStrategy


'''
def set_state(board, row_strings):
    rows_rev = list(map(list, row_strings))
    rows = list(reversed(rows_rev))
    for row in rows:
        i=0
        for c in row:
            if c != Board.EMPTY_CELL:
                board.drop(i, c)
            i += 1

board = Board()

set_state(board, [
    '....',
    'ABBA',
    'ABBA'
])
'''

player_strategies = [RandomStrategy(), MctsStrategy()]

tournament = Tournament(100, player_strategies)
tournament.run()