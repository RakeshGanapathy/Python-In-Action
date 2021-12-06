## Decorators allows us to wrap another function in order to extend the behaviour of the wrapped function ,
##in order to extend the behaviour of the wrapped function, without permanently modifying it
from Anonymous import  sum
def div(a, b):
    print(a / b);


def product(a, b):
    print(a * b)


def smart_opr(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


ans = smart_opr(div)
ans(2, 30)

ans2 = smart_opr(product)
ans2(20, 34)

print(sum)