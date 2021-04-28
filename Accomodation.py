#George and Alex want to live in the same room. The dormitory has n rooms in total. 
# At the moment the i-th room has pi people living in it and the room can accommodate qi people in total (pi ≤ qi). 
# Your task is to count how many rooms has free place for both George and Alex.
count = 0
for i in range(0, int(input())):
    p, q = [int(x) for x in input().split()]
    if abs(p - q) >= 2:
        count += 1
print(count)