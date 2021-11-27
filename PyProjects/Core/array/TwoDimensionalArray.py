from numpy import *

arr1 = array([[2, 3, 4], [4, 5, 6]])
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()

arr3 = arr2.reshape(3, 3)
print(arr2)
