#Check wheter a number is prime or not
def isPrime(n):
    i = 2
    while ( i <= n/2):
        if (n % i == 0):
            print("no")
            break
        i = i + 1
    if (i > n/2):
        return True
    return False

for i in range(int(input())):
    n = int(input())
    if isPrime(n):
        print("It is a prime number")
    else:
        print("It is not a prime number")
    