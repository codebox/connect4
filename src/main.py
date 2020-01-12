from tournament import Tournament
from random_strategy import RandomStrategy
from nn.nn_strategy import NnStrategy
from mcts.mcts_strategy import MctsStrategy
from player import Player
import signal, sys


nn = NnStrategy()
rd = RandomStrategy()
mc = MctsStrategy()

def signal_handler(sig, frame):
    nn.on_end()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

pm = Player('M', mc)
pn = Player('N', nn)
pr = Player('R', rd)

tournament = Tournament(100000, [pm, pn])
tournament.run()
nn.on_end()