# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False)
    return x_test, t_test