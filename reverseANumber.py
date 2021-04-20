def reverse(number):
    num = 0
    while(number > 0):
        num = (10 * num) + (number % 10)
        number //= 10
    return num
number = int(input())
print(reverse(number))