#The difference between the strings equals to the number of positions i, such that S1i is not equal to S2i, where S1i and S2i denote the symbol at the i the position in S1 and S2, respectively.
for i in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    maxdiff = 0
    mindiff = 0
    for j in range(len(s1)):
        if (s1[j] != s2[j] or (s1[j] == '?' and s2[j] == '?')):
            maxdiff += 1
    for j in range(len(s1)):
        if (s1[j] != '?' and s2[j] != '?' and s1[j] != s2[j]):
            mindiff += 1
    print(mindiff,maxdiff)