#You are given an integer number n. Tanya will subtract one from it k times. Your task is to print the result after all k subtractions.
n, k = [int(x) for x in input().split()]
for i in range(0, k):
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1
print(n)