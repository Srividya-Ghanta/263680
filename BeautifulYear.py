#print the next year which contains all unique digits
n=int(input())+1
while len(set(str(n)))<4:n+=1
print(n)