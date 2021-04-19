#There are n stones on the table in a row, each of them can be red, green or blue.
#  Count the minimum number of stones to take from the table so that any two neighboring stones had different colors.
#  Stones in a row are considered neighboring if there are no other stones between them
count = 0
n = int(input())
string = input()
for i in range(1, n):
    if string[i - 1] == string[i]:
        count += 1
print(count)