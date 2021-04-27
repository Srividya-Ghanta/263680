#a matrix looks beautiful, if the single number one of the matrix is located in its middle
#  (in the cell that is on the intersection of the third row and the third column).
#  Count the minimum number of moves needed to make the matrix beautiful.
a = []
for i in range(5):
    a = a+[int(x) for x in input().split()]
ai = a.index(1)
print(abs(2 - (ai // 5)) + abs(2 - (ai % 5)))