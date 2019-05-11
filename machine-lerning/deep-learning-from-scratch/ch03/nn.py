# -*- coding: utf-8 -*-

import numpy as np

def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

def identity_func(x):
    return x

def neural_network():
    # input
    X = np.array([1.0, 0.5])

    #1層
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    B1 = np.array([0.1, 0.2, 0.3])

    A1 = np.dot(X, W1) + B1
    Z1 = sigmoid_func(A1)
    print(Z1)

    # 2層
    W2 = np.array([[0.1, 0.4],[0.2, 0.5],[0.3, 0.6]])
    B2 = np.array([0.1, 0.2])
    
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid_func(A2)
    print(Z2)

    # 3層
    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    B3 = np.array([0.1, 0.2])
    
    A3 = np.dot(Z2, W3) + B3
    Y = identity_func(A3)
    print(Y)

if __name__ == "__main__":
    neural_network()