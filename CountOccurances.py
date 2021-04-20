def countOccurance(num, numbers):
    for i in numbers:
        print(i.count(num))
print("what number do you want to count")
num = input()
test = int(input("number of test cases:"))
numbers = []
for i in range(test):
    numbers.append(input())
countOccurance(num, numbers)