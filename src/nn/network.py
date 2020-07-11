import numpy as np
from keras.models import Sequential, load_model
from abc import ABC, abstractmethod
import os

save_dir = '../saved_models'


class Network(ABC):
    def __init__(self, model):
        self.model = model
        self.load()

    def eval_position(self, board_state):
        input = self._board_states_to_inputs([board_state])
        result = self.model.predict(input)
        return result

    def update(self, board_states, rewards):
        inputs = self._board_states_to_inputs(board_states)
        outputs = np.array(rewards)
        self.model.train_on_batch(inputs, outputs)

    def load(self):
        model_path = os.path.join(save_dir, self.get_save_file())
        if os.path.isfile(model_path):
            self.model = load_model(model_path)
            print(('Loaded model from', model_path))
    
    def save(self):
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        model_path = os.path.join(save_dir, self.get_save_file())
        self.model.save(model_path)

    def _board_states_to_inputs(self, board_states):
        inputs = np.array(board_states)
        inputs = np.expand_dims(inputs, axis=3)

        return inputs

    @abstractmethod
    def get_save_file(self):
        pass

    @abstractmethod
    def get_name(self):
        pass