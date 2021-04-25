#program to take two numbers as input and print their difference if the first number is greater than the second number otherwise print their sum
number1 = int(input())
number2 = int(input())
if number1 > number2:
    print(number1 - number2)
else:
    print(number1 + number2)