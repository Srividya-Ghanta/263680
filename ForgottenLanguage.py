t=int(input())
while(t>0):
    t=t-1
    n,k=list(map(int,input().split()))
    arr=list(map(str,input().split()))
    d={}
    for i in range(k):
        s=input().split()
        for j in s:
            if j not in d:
                d[j]=1
            else:
                d[j]=d[j]+1
    for i in arr:
        if i in d:
            print("YES",end=" ")
        else:
            print("NO",end=" ")