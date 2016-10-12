import numpy as np


class Functions(object):
    def __init__(self, data, func_type):
        self.input = data
        self.func_type = func_type

    def func(self):
        options = {
            'sigmoid': self.sigmoid(),
            'cross_entropy': self.cross_entropy()
        }
        return options[self.func_type]()

    def deri(self):
        options = {
            'sigmoid_prime': self.sigmoid_prime(),
            'cross_entropy_prime': self.cross_entropy_prime()
        }
        return options[self.func_type]

    def sigmoid(self):
        activation = 1.0/(1+np.exp(-self.input))
        return activation

    def sigmoid_prime(self):
        derivative = self.sigmoid()*(1-self.sigmoid())
        return derivative

    def cross_entropy(self):
        return None

    def cross_entropy_prime(self):
        return None


