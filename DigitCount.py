#Given an 'n' digit number as an input print the number of digits in the number
def countDigits(number):
    digits = 0
    while(number > 0):
        digits += 1
        number //= 10
    return digits
number = int(input("Please Enter the number"))
print(countDigits(number))