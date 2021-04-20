def sumRange(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s
def sumNTimes(n, num):
    final = num
    while(n > 0):
        final = sumRange(final)
        n -= 1
    return final
print("Enter the number you want to add")
num = int(input())
print("Enter the number of times you want to add")
n = int(input())
print(sumNTimes(n, num))