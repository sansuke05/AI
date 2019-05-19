#%%
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
y = x > 0
y = y.astype(np.int)
y

#%%
def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
sigmoid_func(x)

#%%
import numpy as np
A = np.array([1, 2, 3, 4])
print(A)
np.ndim(A)
A.shape
A.shape[0]
B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B)
B.shape
#%%
import numpy as np
A = np.array([[1,2], [3,4]])
A.shape
B = np.array([[5,6], [7,8]])
B.shape
np.dot(A, B)
#%%
import numpy as np
A = np.array([[1,2,3],[4,5,6]])
A.shape
B = np.array([[1,2],[3,4],[5,6]])
B.shape
np.dot(A,B)
#%%
import numpy as np
X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W)
Y = np.dot(X, W)
print(Y)
#%%
import numpy as np
def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
Z1 = sigmoid_func(A1)
print(Z1)

#%%
# ソフトマックス関数
import numpy as np
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)
sum_exp_a = np.sum(exp_a)
print(sum_exp_a)
y = exp_a / sum_exp_a
print(y)
#%%
import numpy as np
a = np.array([1010, 1000, 990])
y = np.exp(a) / np.sum(np.exp(a))
print(y)
c = np.max(a)
a = a - c
print(a)
y = np.exp(a) / np.sum(np.exp(a))
print(y)
#%%
import numpy as np

def softmax_func(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax_func(a)
print(y)
s = np.sum(y)
print(s)
#%%
