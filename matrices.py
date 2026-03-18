import numpy as np

v = np.array([[1.5, 2, 3],['hello', 5, 6]])
print(v.shape)

print(v.shape)    # you just did this
print(v.ndim)     # number of dimensions
print(v.dtype)    # data type

#print (v+1)



a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a + b)
print(a*b)
print(a @ b)