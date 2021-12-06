def fact(iteratorValue):
    total = 1
    while iteratorValue > 0:
        total *= iteratorValue
        iteratorValue = iteratorValue - 1

    return total


def fact2(iteratorValue2):
    f = 1
    for i in range(1, iteratorValue2 + 1):
        f *= i
    return f


def factRecursive(inputValue):
    if inputValue == 0:
        return 1;
    else:
        return inputValue * factRecursive(inputValue - 1);


value = int(input("enter the input \n"))
result = factRecursive(value)
print(result)
