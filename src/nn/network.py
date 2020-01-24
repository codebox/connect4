import keras
import numpy as np
from keras.models import Sequential, load_model
from abc import ABC, abstractmethod
import os

batch_size = 32
num_classes = 10
epochs = 100

save_dir = '.'

class Network(ABC):
    def __init__(self, model):
        self.model = model
        self.load()

    def eval_position(self, board_state):
        input = self._board_state_to_input(board_state)
        result = self.model.predict(input)
        return result

    def update(self, board_state, reward):
        input = self._board_state_to_input(board_state)
        output = np.array([reward])
        self.model.train_on_batch(input, output)

    def load(self):
        model_path = os.path.join(save_dir, self.get_save_file())
        if os.path.isfile(model_path):
            self.model = load_model(model_path)
            print('Loaded model from', model_path)
    
    def save(self):
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        model_path = os.path.join(save_dir, self.get_save_file())
        self.model.save(model_path)
        print('Saved trained model at %s ' % model_path)

    def _board_state_to_input(self, board_state):
        input = np.array(board_state)
        input = np.expand_dims(input, axis=2)
        input = np.expand_dims(input, axis=0)

        return input

    @abstractmethod
    def get_save_file(self):
        pass