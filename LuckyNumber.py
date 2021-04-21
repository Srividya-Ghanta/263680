#A number is a lucky number when it contains only 4 and 7 as its digits
def checkDigits(number):
    while(number > 0):
        if number % 10 == 4 or number % 10 == 7:
            number //= 10
        else:
            return False
    return True

number = int(input())
if checkDigits(number):
    print("It is a lucky number")
else:
    print("It is not a lucky number")