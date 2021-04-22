number = int(input("enter the number of tuples to input:"))
tuple_list = []
dictionary = {}
for i in range(number):
    a , b = [int(x) for x in input().split()]
    tuple_list.append((a,b))
for a,b in tuple_list:
    dictionary.setdefault(a, []).append(b)
print(dictionary)