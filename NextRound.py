#Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round,
#  as long as the contestant earns a positive scoreA total of n participants took part in the contest (n ≥ k), 
# and you already know their scores. Calculate how many participants will advance to the next round.
n,k = map(int,input().split())
a = list(map(int,input().split()))
coun = 0
for i in range(n):
    if(a[i] > 0):
        if(a[i] >= a[k - 1]):
            coun = coun + 1
print(coun)
