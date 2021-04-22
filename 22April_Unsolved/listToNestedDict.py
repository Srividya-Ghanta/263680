print("Enter the list elements: ")
li = [int(x) for x in input().split()]
dictionary = current = {}
for i in li:
    current[i] = {}
    current = current[i]
print(dictionary)