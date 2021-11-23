# collection of unique elements , we can identify set using {} curly brackets
# it stores the element randomly not sequentially
# as like list , the set will not maintain insertion order

unique = {21, 23, 34, 56, 78, 90}
print(unique)
unique.pop()
print(unique)
print(len(unique))
unique.add(78)
print(unique.issubset(unique))
print(unique.issuperset({34, 21}))

print(unique)
