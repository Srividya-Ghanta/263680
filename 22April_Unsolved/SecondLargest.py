print("Enter the list elements")
li = [int(x) for x in input().split()]
maximum = max(li)
while(maximum in li):
    li.remove(maximum)
print("The second largest element is:", max(li))