#For a positive integer n let's define a function f:
#f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn
#Your task is to calculate f(n) for a given integer n.
num = int(input())
sum = 0
if num % 2 == 0:
    sum = num // 2
    print(sum)
else:
    sum = -((num + 1) // 2)
    print(sum)