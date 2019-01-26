from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation, Flatten, Dense
from keras import backend


class ShallowNet:

    @staticmethod
    def build(width, height, depth, classes):

        #Initilize model; input shape is as follows
        model = Sequential()
        inputShape = (height, width, depth)

        #If we use channels first
        #update the input

        if backend.image_data_format() == "channels_first":
            inputShape = (depth, height, width)

        #Add Layer
        #Conv => RELU

        model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))

        #Add softmax classifier
        model.add(Flatten()) #Flatten Multi dimensional represeantation
        model.add(Dense(classes)) #Layer created using same number of nodes as output layer
        model.add(Activation("softmax")) #Applies a softmax classifier for probs of class labels


        return model

