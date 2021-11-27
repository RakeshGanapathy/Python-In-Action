from array import *

arr = array('i', [])

inputCount = int(input("how many input you need to add \n"))
for i in range(inputCount):
    x = int(input("enter the value : "))
    arr.append(x)  # adds the value to the array

print(arr)

searchValue = int(input("enter the value to search "))
k = 0
for element in arr:
    if element == searchValue:
        print(k)
        break
    k += 1
