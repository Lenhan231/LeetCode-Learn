import numpy as np  # optional
a = [1,2,3,4]
a = np.array(a)
print(a) #array are designed to handle vectorized operation
a += 2
print(a) # difference between array and list
a = [[1,2,3],[3,4,5]]
a = np.array(a)
print(a) # 2d array which 1 2 3 is row 1 and 3 4 5 is row 2
arr2d_b = np.array([1, 0, 10], dtype='bool')
print(arr2d_b)
arr1d_obj = np.array([1, 'a'], dtype='object')
arr1d_obj = arr1d_obj.tolist()
print(arr1d_obj)
# to explore an non-self create array the first thing to do
# - shape, type, size, dim
print(a.shape)
print(a.size)
print(a.dtype)
print(a.ndim)

arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(out)
