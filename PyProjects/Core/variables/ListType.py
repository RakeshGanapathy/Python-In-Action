nums = [25, 12, 36, 95, 14]

# returns the first element by using both +ve and -ve ranges 25
print(nums[0])
print(nums[-5])

names = ["rakesh", "ranjith", "sandy"]

values = [9.3, "appu"]

names.append("kavin")
names.insert(2, "abi")
names.sort()

# appends the whole list as an element in the another list
# [9.3, 'appu', ['abi', 'kavin', 'rakesh', 'ranjith', 'sandy']]
values.append(names)
print(values)

# [['abi', 'kavin', 'rakesh', 'ranjith', 'sandy'], [9.3, 'appu', ['abi', 'kavin', 'rakesh', 'ranjith', 'sandy']]]
combination = [names, values]
print(combination)

# pop() method removes the last element
print(names.pop())
# pop(index) will remove the element in index specified
print(names.pop(1))

# removes the element called "abi"
names.remove("abi")
print(names)
# add multiple values in the list
names.extend(["trip", "holiday", "game", "politics"])

nums.extend([20, 34, 56.67])
print(nums)

print(sum(nums))
print(min(nums))
print(max(nums))
nums.sort()
print(nums)

print("total sum is " + sum(nums).__str__())

# to remove the multiple values of elements specified
print(names)
# ['rakesh', 'ranjith', 'trip', 'holiday', 'game', 'politics']
del names[4:]
# ['rakesh', 'ranjith', 'trip', 'holiday']
print(names)
