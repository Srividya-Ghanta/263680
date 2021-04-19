string = input()
s1 = ''
s = sorted([int(x) for x in string.split('+')])
for i in range(len(s) - 1):
    s1 += str(s[i]) + '+'
s1 += str(s[-1])
print(s1)