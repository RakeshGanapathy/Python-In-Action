def fibonacci(i):
    f1 = 0
    f2 = 1
    print(f1)
    print(f2)

    for ele in range(2, i):
        f3 = f1 + f2
        print(f3)
        f1 = f2
        f2 = f3


count = int(input("enter the input"))
fibonacci(count)
