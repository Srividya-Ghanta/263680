print("Enter the list elements:")
li = [int(x) for x in input().split()]
for i in range(0, len(li)-1):
    li[i],li[i+1] = li[i+1],li[i]
print(li)