print("Enter the list elements")
li = [int(x) for x in input().split()]
minimum = min(li)
while(minimum in li):
    li.remove(minimum)
print("Second smallest element is", min(li))