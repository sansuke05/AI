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
