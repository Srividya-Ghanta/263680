#What is the maximum number of squares of size 2x2 that can be fit in a right angled isosceles triangle of base B.
test = int(input())
s = 0
while(test > 0):
    n = int(input())
    for i in range(1, (n // 2)):
        s += i
    print(s)
    s = 0