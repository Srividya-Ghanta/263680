#calculate the tram's minimum capacity such that the number of people inside the tram at any time never exceeds this capacity
n = int(input())
k = 0
max = 0
for  i in range(n):
    a, b = list(map(int, input().split()))
    k = k - (a - b)
    if k > max:
        max = k
print(max)