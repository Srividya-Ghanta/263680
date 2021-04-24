def reverse(number):
    rev = 0
    while(number > 0):
        rev = rev * 10 + (number % 10)
        number //= 10
    return rev
def first_last(number):
    print("first digit is",reverse(number)% 10)
    print("last digit is:", number % 10)
    
number = int(input())
print(first_last(number))