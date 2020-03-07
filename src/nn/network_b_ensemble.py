from nn.network_128x4_64_64 import NetworkB
from nn.network import Network

class NetworkBEnsemble(Network):
    def __init__(self, id=''):
        self.id = id

        super().__init__(EnsembleModel(3))

    def get_save_file(self):
        return 'does not exist'

    def get_name(self):
        return 'B-Ensemble'

class EnsembleModel():
    def __init__(self, count):
        self.nets = [NetworkB(i+1) for i in range(count)]

    def predict(self, input):
        return sum([net.model.predict(input) for net in self.nets]) / len(self.nets)

    def train_on_batch(self, inputs, outputs):
        pass

    def save(self, path):
        pass

