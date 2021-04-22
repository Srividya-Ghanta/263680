tup = (1 , 2, 3, "hello", "how", "hello", 3, 4, 2, 1, 5)
unique = list(set(tup))
repeated = []
for i in unique:
    if tup.count(i) > 1:
        repeated.append(i)
print(repeated)