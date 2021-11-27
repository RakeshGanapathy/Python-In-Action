for i in range(2000, 2060):
    if i % 4 != 0:
        pass   # will skip the year
    else:
        print("{} is a leap year".format(i))
