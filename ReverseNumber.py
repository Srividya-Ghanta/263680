def reverse_of_number(number):
    reverse = 0
    while(number > 0):
        reverse = reverse * 10 + (number % 10)
        number //= 10
    return reverse
test = int(input())
for i in range(test):
    number = int(input())
    print(reverse_of_number(number))