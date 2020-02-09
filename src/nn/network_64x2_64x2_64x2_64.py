import keras
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from nn.network import Network

batch_size = 32
num_classes = 10
epochs = 100

save_dir = '.'

class NetworkC(Network):
    def __init__(self):
        model = Sequential()
        model.add(Conv2D(64, (2, 2), input_shape=(6, 7, 1)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (2, 2)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (2, 2)))
        model.add(Activation('relu'))

        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dense(1))

        opt = keras.optimizers.Adam()

        model.compile(loss='mean_squared_error',
                      optimizer=opt,
                      metrics=['accuracy'])

        super().__init__(model)

    def get_save_file(self):
        return 'model_64-2_64-2_64-2_64.h5'

    def get_name(self):
        return 'C'