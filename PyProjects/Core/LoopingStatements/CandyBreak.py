stock = 10
x = int(input("how many candies you need : "))
i = 1
while i <= x:

    if i > stock:
        print("out of stock")
        break

    print("candy")
    i += 1

print("Bye")
