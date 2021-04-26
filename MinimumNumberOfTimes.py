for i in range(int(input())):
    a = list(map(int, input().split()))
    mini = max(a)
    maxi = sum(a)
    print(str(mini) + " " + str(maxi))