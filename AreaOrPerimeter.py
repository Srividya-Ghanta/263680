#program to obtain length (L) and breadth (B) of a rectangle and check whether its area is greater or perimeter is greater or both are equal.
length = int(input())
breadth = int(input())
area = (length * breadth)
perimeter = (2 * length + 2 * breadth)
if area > perimeter:
    print('Are is greater')
else:
    print("perimeter is greater")