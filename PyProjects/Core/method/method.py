def greet():
    print("greet")
    print("fun")


def add(x, y):
    z = x + y;
    return z;


def methodSignature(a, *b):
    c = a
    print(a)
    print(b)
    for element in b:
        c += element

    print(c)


def items(name, **kwargs):
    print(name)
    print(kwargs)

    for ele in kwargs:
        print(ele)

# returning 2 variables
def countOfEvenOdd(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd





items("rakesh ", moto='fun', vehicle='neon', bike='bullet')

greet()
result1 = add(34, 45)
print(result1)

result2 = add(y=34, x=12)
print(result1, result2)
methodSignature(23, 45, 23, 34)
even ,odd = countOfEvenOdd([23,34,45,67,78,23,1,2])
print ("even {}".format(even))
print("odd {}".format(odd))

