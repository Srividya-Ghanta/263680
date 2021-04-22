print("Enter the elements")
li = [int(x) for x in input().split()]
unique = set(li)
print("Maximum element in the set:",max(unique))
print("Minimum element in the set:",min(unique))