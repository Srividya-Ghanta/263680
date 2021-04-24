def sum_of_digits(number):
    digit_sum = 0
    while(number > 0):
        digit_sum += (number % 10)
        number //= 10
    return digit_Sum
test = int(input())
for i in range(test):
    number = int(input())
    print(sum_of_digits(number))