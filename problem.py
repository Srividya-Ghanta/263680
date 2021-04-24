test = int(input())
difficulty = [int(x) for x in input().split()]
if difficulty.count(1) > 0:
    print("the problem in hard")
else:
    print("the problem is easy")