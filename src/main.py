from tournament import Tournament
from random_strategy import RandomStrategy
from nn.nn_strategy import NnStrategy
from nn.network_64x2_64x2_64_64 import NetworkA
from nn.network_128x4_64_64 import NetworkB
from nn.network_64x2_64x2_64x2_64 import NetworkC
from nn.network_64x4_64x2_64x2_64 import NetworkD
from mcts.mcts_strategy import MctsStrategy
from player import Player
import signal, sys

from keras import backend as K

nn_a = NnStrategy(NetworkA())
nn_b = NnStrategy(NetworkB())
nn_c = NnStrategy(NetworkC())
net_d = NetworkD()
nn_d1 = NnStrategy(net_d)
nn_d2 = NnStrategy(net_d)
rd = RandomStrategy()
mc = MctsStrategy()

def signal_handler(sig, frame):
    tournament.close()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

pm  = Player('M', mc)
pna = Player('A', nn_a) # 64-2 64-2 64 64
pnb = Player('B', nn_b) # 128-4 64 64
pnc = Player('C', nn_c) # 64-2 64-2 64-2 64
pnd1 = Player('D', nn_d1) # 64x4_64x2_64x2_64
pnd2 = Player('X', nn_d2) # 64x4_64x2_64x2_64
pr  = Player('R', rd)

for i in range(1000):
    print('tournament',i)
    tournament = Tournament(1000, [pnd1, pnd2])
    tournament.run()
