# sum(D, N), which means the operation sum applied D times: the first time to N, and each subsequent time to the result of the previous operation.
for i in range(int(input())):
    d, n = [int(x) for x in input().split()]
    s = 0
    while(d > 0):
        s = ((n*(n+1))//2)
        n = s
        d -= 1
    print(s)