#You are given a sequence a1, a2, ..., aN. Find the smallest possible value of ai + aj, where 1 ≤ i < j ≤ N.
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = min(a)
    a.remove(mini)
    mini2 = min(a)
    sum = mini + mini2
    print(sum)