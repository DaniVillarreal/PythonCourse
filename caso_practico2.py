
from math import e

"""RNA activation functions"""

"""ReLu activation function"""

def relu(x):
    """Calculate the result of the mathematical function ReLu"""
    return max(0, x)

"""Sigmoid activation function"""

def sigmoid(x):
    """Calculate the result of the mathematical function Sigmoid"""
    return 1 / (1 + e**-x)

"""Tanh activation function"""

def sinh(x):
    """Calculate the result of the mathematical function sinh"""
    return (e**x + e**-x) / 2

def cosh(x):
    """Calculate the result of the mathematical function cosh"""
    return (e**x + e**-x) / 2

def tanh(x):
    """Calculate the result of the mathematical function tenh"""
    return sinh(x) / cosh(x)


def run():
    """ReLu"""
    print("\nTEST RELU")
    print(relu(0))

    print(relu(-10))

    print(relu(5))

    """Sigmoid"""

    print("\nTEST SIGMOID")
    print(sigmoid(0))

    print(sigmoid(5))

    print(sigmoid(-2.5))


    """Tanh"""

    print("\nTEST TANH")
    print(tanh(-10))

if __name__ == "__main__":
    run()