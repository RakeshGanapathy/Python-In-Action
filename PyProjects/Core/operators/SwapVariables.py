a = 5
b = 6

temp = a
a = b;
b = temp

print(a)
print(b)

# approach 2

a = a + b
b = a - b
a = a - b

print(a)
print(b)

# approach 3

a, b = b, a


