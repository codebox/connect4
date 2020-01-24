import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from nn.network import Network

class NetworkB(Network):
    def __init__(self):
        model = Sequential()
        model.add(Conv2D(128, (4,4), input_shape=(6, 7, 1)))
        model.add(Activation('relu'))

        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dense(1))

        # opt = keras.optimizers.RMSprop(learning_rate=0.0001)
        opt = keras.optimizers.Adam()

        model.compile(loss='mean_squared_error',
                      optimizer=opt,
                      metrics=['accuracy'])

        super().__init__(model)

    def get_save_file(self):
        return 'model_128-4_64_64.h5'