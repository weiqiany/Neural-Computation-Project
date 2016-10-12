import numpy as np
import Functions as F
import random


class Neural_Network(object):
    def __init__(self, sizes):
        self.sizes = sizes
        self.layers = len(sizes)
        self.biases = [np.random.randn(1, y) for y in sizes]
        self.weights = [np.random.randn(x, y) for x, y in zip(sizes[:-1], sizes[1:])]

    def acti_function(self, data, func_type):
        data = data
        func_type = func_type
        activation= F.Functions(data, func_type).func()
        return activation

    def deri_function(self, data, func_type):
        data = data
        func_type = func_type
        derivation = F.Functions(data, func_type).deri()
        return derivation

    def feedford(self, data):
        nodes = data
        for w, b in zip(self.weights, self.biases):
            nodes = self.acti_function(np.dot(w, nodes) + b, 'sigmoid')
        return nodes

    def SDG(self, data, epochs, mini_batch_size, eta):
        l = len(data)
        for j in xrange(epochs):
            random.shuffle(data)
            mini_batches = [data[k:k+mini_batch_size] for k in xrange(0, l, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)

    def update_mini_batch(self, mini_batch, eta):
