# tuple is same as list where its immutable, i.e we cannot change the value
# we use round bracket () for tuple
tup = (2,3,21,22, 234,232,65,23, 23, 34, 56)
i = tup.count(23)
# sort is no possible in tuple
# index returns the index value of the element
print("index value of 21 in the tuple is "+tup.index(21).__str__())
print(tup)
print(i)
