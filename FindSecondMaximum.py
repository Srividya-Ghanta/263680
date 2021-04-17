n = int(input())
arr = [int(x) for x in input().split()]
maximum = max(arr)
while maximum in arr:
    arr.remove(maximum)
print(max(arr))