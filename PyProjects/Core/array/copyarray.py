from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 5, 3, 7, 1])

arr3 = arr1 + arr2

print(arr3)

print(sin(arr3))
print(sqrt(arr3))
print(sum(arr3))
print(min(arr3))
print(max(arr3))
print(average(arr3))
print(concatenate([arr1, arr2]))

# shallow copy
copyarr = arr1
print(copyarr)
print(arr1)

# print the address
print(id(arr1))
print(id(copyarr))

# proper copy with different memory address
copyArray = arr1.copy()
print(id(copyArray))


