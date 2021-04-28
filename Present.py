n = int(input())
a = [int(x) for x in input().split()]
v = []
for i in range(len(a)):
    v.insert((a[i]-1), (i + 1))
for i in v:
    print(i,)
