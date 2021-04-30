#The task was to insert signs of operations '+' and '*', and probably brackets between the numbers so that the value of
#  the resulting expression is as large as possible.
a = int(input())
b = int(input())
c = int(input())
arr = []
arr.append(a+b+c)
arr.append(a*b*c)
arr.append((a+b)*c)
arr.append(a+(b * c))
arr.append((a*b)+c)
arr.append(a * (b + c))
print(max(arr))