#You are given a string.
#  Your task is to determine whether number of occurrences of some character in the string is equal to the sum of the numbers of 
# occurrences of other characters in the string. 

for i in range(int(input())):
    s = input()
    c = []
    flag = 1
    st = list(set(s))
    for j in st:
        c.append(s.count(j))
    for j in range(len(c)):
        if c[j] == sum(c)-c[j]:
            flag = 0
            print("YES")
            break
    if flag == 1:
        print("NO")