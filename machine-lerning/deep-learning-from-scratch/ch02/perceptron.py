# -*- coding: utf-8 -*-
import numpy as np

def and_gate(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    formula = x1*w1 + x2*w2
    if formula <= theta:
        return 0
    elif formula > theta:
        return 1


def and_with_b(x1, x2):
    x = np.array([x1, x2])      # input vector
    w = np.array([0.5, 0.5])    # weight vector
    b = -0.7                    # bias(バイアス)
    f = np.sum(w*x) + b
    if f <= 0:
        return 0
    elif f > 0:
        return 1


def nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # nandなので逆数のweightにする
    b = 0.7                     
    f = np.sum(w*x) + b
    if f <= 0:
        return 0
    elif f > 0:
        return 1


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    f = np.sum(w*x) + b
    if f <= 0:
        return 0
    elif f > 0:
        return 1


def xor(x1, x2):
    s1 = nand(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_with_b(s1, s2)
    return y

if __name__ == "__main__":
    print(xor(0, 0))
    print(xor(1, 0))
    print(xor(0, 1))
    print(xor(1, 1))