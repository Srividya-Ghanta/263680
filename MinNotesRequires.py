for i in range(int(input())):
    n = int(input())
    count = 0
    while (n > 0):
        if (n >= 100):
            n = n - 100
        elif n >= 50:
            n = n - 50
        elif n >= 10:
            n -= 10
        elif n >= 5:
            n -= 5
        elif n >= 2:
            n -= 2
        else:
            n -= 1
        count += 1
    print("Minimum number of notes required are:",count)        