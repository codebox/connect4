from tournament import Tournament
from random_strategy import RandomStrategy
from nn.nn_strategy import NnStrategy
from nn.network_64x2_64x2_64_64 import NetworkA
from nn.network_128x4_64_64 import NetworkB
from nn.network_64x2_64x2_64x2_64 import NetworkC
from nn.network_64x4_64x2_64x2_64 import NetworkD
from nn.network_256x4_64_64 import NetworkE
from nn.network_b_ensemble import NetworkBEnsemble
from nn.nn_minimax_strategy import NnMiniMaxStrategy
from mcts.mcts_strategy import MctsStrategy
from player import Player
import signal, sys, itertools
import math

def signal_handler(sig, frame):
    tournament.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


# networks = [NetworkA(), NetworkB(), NetworkC(), NetworkD()]
# benchmark_strategies = [RandomStrategy(), MctsStrategy(10), MctsStrategy(50), MctsStrategy(250)]#, MctsStrategy(1000)]
# networks = [NetworkB()]
# benchmark_strategies = [MctsStrategy(1000)]#, MctsStrategy(1000)]
# n_b1 = NetworkB1()
# n_b2 = NetworkB2()
# b1_player = Player('B',n_b1)
# b2_player = Player('b',n_b2)

tournament=None
self_play_batch_size=10000
benchmark_batch_size=10
training_rounds=1000

def get_exploration_factor(game_number):
    # return 0.1 * math.pow(1 - 0.000002, game_number)
    return 0.1

def log(msg):
    with open('../log.txt', 'a') as f:
        f.write(msg + '\n')

# for round in range(0,training_rounds):
#     print('Benchmarking before round', round)
#     for benchmark in benchmark_strategies:
#         # for network in networks:
#         ns = NnStrategy(n_b1)
#         p1 = Player('N', ns)
#         p2 = Player('B', benchmark)
#         tournament = Tournament(benchmark_batch_size, [p1, p2])
#         results = tournament.run(False)
#         print('Results for {} vs {}: {}'.format(benchmark.get_name(), ns.get_name(), results))
#         log('{},{}:{},{}:{}'.format((round-1) * self_play_batch_size, ns.get_name(), results.get('N', 0), benchmark.get_name(),results.get('B', 0)))
#
#     print('Starting round', round)
#     # for network in networks:
#     # print('Self-play training ' + network.get_name(), end='', flush=True)
#     print('Self-play training')
#     p1 = Player('1', NnStrategy(n_b1, get_exploration_factor))
#     p2 = Player('2', NnStrategy(n_b2, get_exploration_factor))
#     tournament = Tournament(self_play_batch_size, [p1, p2])
#     tournament.run(True, lambda r: print('.', end='', flush=True))
#     print('')
#
#     print('- - - - - - - - - -')


def self_play_group(count):
    global tournament
    networks = [NetworkB(i+1) for i in range(count)]
    strategies = [NnStrategy(n, get_exploration_factor) for n in networks]
    players = [Player('B' + str(i), s) for i,s in enumerate(strategies)]

    for round in range(1,training_rounds):
        print('Benchmarking before round', round)

        for benchmark in [MctsStrategy(1000)]:
            for network in networks:
                ns = NnStrategy(network)
                p1 = Player('N', ns)
                p2 = Player('B', benchmark)
                tournament = Tournament(benchmark_batch_size, [p1, p2])
                results = tournament.run(False)
                print('Results for {} vs {}: {}\n'.format(benchmark.get_name(), ns.get_name(), results))
                log('{},{}:{},{}:{}'.format((round-1) * self_play_batch_size, ns.get_name(), results.get('N', 0), benchmark.get_name(),results.get('B', 0)))

        for p1,p2 in itertools.combinations(players,2):
            tournament = Tournament(self_play_batch_size, [p1, p2])
            tournament.run(True)

        print('- - - - - - - - - -')


# self_play_group(3)

def test_ensemble():
    p1 = Player('N', NnStrategy(NetworkBEnsemble('N')))
    p2 = Player('X', MctsStrategy(1000))
    tournament = Tournament(100, [p2, p1])
    result = tournament.run(False)
    print(result)

# test_ensemble()

def test_minimax(lookahead_limit):
    mms = NnMiniMaxStrategy(NetworkBEnsemble('N'), lookahead_limit, ['N', 'X'])
    p1 = Player('N', mms)
    p2 = Player('X', MctsStrategy(1000))
    tournament = Tournament(100, [p2, p1])
    result = tournament.run(False)
    print(' ')
    print(lookahead_limit, result, mms.average_move_time(),flush=True)

self_play_group(3)
[test_minimax(n) for n in range(0,3)]
