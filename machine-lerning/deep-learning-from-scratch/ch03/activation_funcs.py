# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def step_func_scalars_only(x):
    if x > 0:
        return 1
    else:
        return 0


def step_func_for_np_array(x):
    y = x > 0 #各要素に対して演算 -> boolean
    return y.astype(np.int)


def step_func(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))


def plot():
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid_func(x)
    plt.plot(x,y)
    plt.ylim(-0.1, 1.1)
    plt.show()


if __name__ == "__main__":
    #print(step_func_scalars_only(1-2*0.5))
    plot()