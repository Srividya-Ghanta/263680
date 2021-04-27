#Consider the width of the person walking as usual to be equal to 1, while the width of the bent person is equal to 2.
#  Friends want to talk to each other while walking, so they would like to walk in a single row. 
# What is the minimum width of the road, such that friends can walk in a row and remain unattended by the guard?
n, h = [int(x) for x in input().split()]
friends = [int(x) for x in input().split()]
width = 0

for i in friends:
    if i > h:
        width += 2
    elif i <= h:
        width += 1
print(width)