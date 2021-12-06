from functools import reduce

nums = [23, 34, 56, 45, 56, 67, 78]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n * 2, evens))
print(doubles)

sum = reduce(lambda a, b: a + b, doubles)
print (sum)