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
