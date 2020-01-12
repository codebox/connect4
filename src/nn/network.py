import keras
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os

batch_size = 32
num_classes = 10
epochs = 100

save_dir = '.'
save_file = 'keras_connect4_trained_model.h5'

class Network:
    def __init__(self, rows, cols):
        self.model = Sequential()
        self.model.add(Conv2D(64, (2, 2), input_shape=(rows, cols, 1)))
        self.model.add(Activation('relu'))
        self.model.add(Conv2D(64, (2, 2)))
        self.model.add(Activation('relu'))

        self.model.add(Flatten())
        self.model.add(Dense(64))
        self.model.add(Activation('relu'))
        self.model.add(Dense(64))
        self.model.add(Activation('relu'))
        self.model.add(Dense(1))

        # opt = keras.optimizers.RMSprop(learning_rate=0.0001)
        opt = keras.optimizers.SGD(lr=0.00001, decay=1e-6)

        self.model.compile(loss='mean_squared_error',
                      optimizer=opt,
                      metrics=['accuracy'])

    def eval_position(self, board_state):
        input = self._board_state_to_input(board_state)
        result = self.model.predict(input)
        return result

    def update(self, board_state, reward):
        input = self._board_state_to_input(board_state)
        output = np.array([reward])
        self.model.train_on_batch(input, output)

    def load(self):
        model_path = os.path.join(save_dir, save_file)
        if os.path.isfile(model_path):
            self.model = load_model(model_path)
            print('Loaded model from', model_path)
    
    def save(self):
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        model_path = os.path.join(save_dir, save_file)
        self.model.save(model_path)
        print('Saved trained model at %s ' % model_path)

    def _board_state_to_input(self, board_state):
        '''
        [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]
        '''
        input = np.array(board_state)
        input = np.expand_dims(input, axis=2)
        input = np.expand_dims(input, axis=0)

        return input