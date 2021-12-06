from math import pow

inputValue = int(input("Enter the input number \n"))

digits = len(str(inputValue));
print(digits)
temp = inputValue
result = 0

while temp > 0:
    num = temp % 10
    temp //= 10
    result += pow(num, digits)

if inputValue == result:
    print('the input {} is an armstrong number'.format(inputValue))
else:
    print('the input {} is not an armstrong number'.format(inputValue))
