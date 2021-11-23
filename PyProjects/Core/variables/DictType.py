# dictionary is used to store key value pairs
data = {1: 'rakesh', 2: 'praveen', 3: 'divya'}
print(data[3])

name = data.get(1)
print(name)

# not sure whether the key is present or not then go with get(key, message)
print(data.get(4,"Not Found"))

value = data.__getitem__(2)
print(value)