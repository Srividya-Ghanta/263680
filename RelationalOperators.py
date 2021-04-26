#Given two numerical values A and B you need to help chef in finding the relationship between them that is, A> B or A < B or A == B
A = int(input())
B = int(input())
if A > B:
    print("First is greater than second")
elif A < B:
    print("First is less than second")
else:
    print("First and second are equal")