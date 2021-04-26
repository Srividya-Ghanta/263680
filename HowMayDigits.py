#Program to obtain a number and print how many digits number is it
def digitCount(number):
    digits = 0
    while(number > 0):
        digits += 1
        number //= 10
    return digits
number = int(input())
print("the number of digits in the number are:",digitCount(number))