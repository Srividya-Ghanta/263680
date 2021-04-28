#Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.
input();c=m=s=0
for i in map(int,input().split()):c=[c+1,1][i<s];m=max(m,c);s=i
print(m)