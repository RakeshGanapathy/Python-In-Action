
num = 10

for i in range(2, num):
    if num % i == 0:
        print("{} Not Prime".format(i))
    else:
        print("{} Prime".format(i))
