def factorial(number):
    fact = 1
    while(number > 0):
        fact *= number
        number -= 1
    return fact
def main():
    number = int(input())
    print(factorial(number))
if __name__ == '__main__':
    main()
    