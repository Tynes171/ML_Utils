from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense
from keras import backend

class LeNet:

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
        #Conv => RELU => Pool

        model.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(2, 2))

        # Add Layer
        # Conv => RELU => Pool

        model.add(Conv2D(50, (5, 5), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(2, 2))



        #Add softmax classifier
        model.add(Flatten()) #Flatten Multi dimensional represeantation
        model.add(Dense(500)) #Layer created using same number of nodes as output layer
        model.add(Activation("relu")) #Applies a softmax classifier for probs of class labels

       # Add softmax  classifier

        model.add(Dense(classes))  # Layer created using same number of nodes as output layer
        model.add(Activation("softmax"))  # Applies a softmax classifier for probs of class labels


        return model
