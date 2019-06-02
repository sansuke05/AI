# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist

def softmax_func(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

def get_data():
    print('loading mnist dataset...')
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    print('creating prediction network...')
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    #print(W1.shape)
    #print(W2.shape)
    #print(W3.shape)

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid_func(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid_func(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax_func(a3)

    return y

if __name__ == "__main__":
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    print('predicting...')
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y) #最も確率の高い要素のインデックスを取得
        if p == t[i]:
            accuracy_cnt += 1
    
    print('Accuracy:' + str(float(accuracy_cnt) / len(x)))