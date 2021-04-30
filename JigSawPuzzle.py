#The shop assistant told the teacher that there are m puzzles in the shop, but they might differ in difficulty and size. 
# Specifically, the first jigsaw puzzle consists of f1 pieces, the second one consists of f2 pieces and so on.
I=lambda:map(int,input().split())
n,m=I()
a=sorted(I())
print(min(j-i for i,j in zip(a,a[n-1:])))