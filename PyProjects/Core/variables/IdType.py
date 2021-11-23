num = 5
print(id(num))

name = "rakesh"
print(id(name))

a = 10
b = a
print(id(a))
print(id(b))
print(id(10))

# <class 'int'>
print(type(a))

pi = 3.14
# <class 'float'>
print(type(pi))

# <class 'str'>
print(type(name))

# complex
c = 34 + 5j;
print(type(c))

complexNumber = complex(a, b)
print(complexNumber)

bool = 10 < 15
print(bool)
print(type(bool))
print(int(True))  # 1
print(int(False))  # 0
list = [23, 34, 456, 6]

print(type(list))
set = {20, 30, 40}
print(type(set))
tuple = (10, 20, 30)
print(type(tuple))

dict = {20: "rakesh",21:"sandy"}
print(type(dict))
print(range(10))
print(type(range(10)))
print(dict.keys())
print(dict.values())
print(dict.get(20))