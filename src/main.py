from tournament import Tournament
from random_strategy import RandomStrategy
from nn.nn_strategy import NnStrategy
from nn.network_64x2_64x2_64_64 import NetworkA
from nn.network_128x4_64_64 import NetworkB
from nn.network_64x2_64x2_64x2_64 import NetworkC
from nn.network_64x4_64x2_64x2_64 import NetworkD
from nn.network_256x4_64_64 import NetworkE
from mcts.mcts_strategy import MctsStrategy
from player import Player
import signal, sys

def signal_handler(sig, frame):
    tournament.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


# networks = [NetworkA(), NetworkB(), NetworkC(), NetworkD()]
# benchmark_strategies = [RandomStrategy(), MctsStrategy(10), MctsStrategy(50), MctsStrategy(250)]#, MctsStrategy(1000)]
networks = [NetworkB()]
benchmark_strategies = [MctsStrategy(1000)]#, MctsStrategy(1000)]

self_play_batch_size=10000
benchmark_batch_size=10
training_rounds=1000
exploration_factor=0.1

def log(msg):
    with open('../log.txt', 'a') as f:
        f.write(msg + '\n')

for round in range(0,training_rounds):
    print('Benchmarking before round', round)
    for benchmark in benchmark_strategies:
        for network in networks:
            ns = NnStrategy(network)
            p1 = Player('N', ns)
            p2 = Player('B', benchmark)
            tournament = Tournament(benchmark_batch_size, [p1, p2])
            results = tournament.run(False)
            print('Results for {} vs {}: {}'.format(benchmark.get_name(), ns.get_name(), results))
            log('{},{}:{},{}:{}'.format((round-1) * self_play_batch_size, ns.get_name(), results.get('N', 0), benchmark.get_name(),results.get('B', 0)))

    print('Starting round', round)
    for network in networks:
        print('Self-play training ' + network.get_name(), end='', flush=True)
        p1 = Player('1', NnStrategy(network, exploration_factor))
        p2 = Player('2', NnStrategy(network, exploration_factor))
        tournament = Tournament(self_play_batch_size, [p1, p2])
        tournament.run(True, lambda r: print('.', end='', flush=True))
        print('')

    print('- - - - - - - - - -')

