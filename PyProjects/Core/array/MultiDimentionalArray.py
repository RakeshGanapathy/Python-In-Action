from numpy import *

arr = array([2, 3, 4, 5], float)
print(arr)

# install numpy using the command pip3 install numpy


arr1 = array([2, 3, 4, 5], float)
print(arr1.dtype)
print(arr1)

arr2 = linspace(0, 15, 20)  # takes 3 param, start , stop , parts gap between two element is fixed
print(arr2)

arr2 = linspace(0, 15, 20)  # takes 3 param, start , stop  by default will create 50 parts
print(arr2)
arr3 = logspace(1, 40, 15)
print(arr3)

# arange

arr4 = arange(1, 15, 2)  # start , stop , skip the steps [ 1  3  5  7  9 11 13]

print(arr4)

arr5 = zeros(4)
print(arr5)

arr6 = ones(4, float)
print(arr6)
