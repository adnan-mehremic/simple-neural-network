# Simple neural network

import math
import random

class NeuralNetwork():

    def __init_(self):
        random.seed(1)
        self.weights = [random.uniform(-1, 1),
                        random.uniform(-1,1),
                        random.uniform(-1,1)]

    def think(self, neuron_inputs):
        sum_of_weighted_inputs = self.__sum_of_weighted_inputs(neuron_inputs)
        neuron_output = self.__sigmoid(sum_of_weighted_inputs)
        return neuron_output

    def train(self):
        pass

    def __sigmoid(self):
        pass

    def __sigmoid_gradient(self):
        pass

    def __sum_of_weighted_inputs(self):
        pass

# Traning set for neural network
training_set_examples = [{'inputs': [0, 0, 1], 'output': 0},
                         {'inputs': [1, 1, 1], 'output': 1},
                         {'inputs': [1, 0, 1], 'output': 1},
                         {'inputs': [0, 1, 1], 'output': 1}]

