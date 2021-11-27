from array import *
values = array('I', [2, 3, 4, 5, 1, 2])
print(values)
for i in values:
    print(i)

newArr = array(values.typecode, [a*a for a in values])
print (newArr)

for i in newArr:
    print(i)