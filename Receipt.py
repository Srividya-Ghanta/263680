for i in range(int(input())):
    p = int(input())
    c = 0
    if p <= 2048:
        print(bin(p).replace('0b', "").count('1'))
        continue
    else:
        c = p // 2048
        p = p - 2048*(c)
        print(c + bin(p).replace("0b", "").count('1'))