for i in range(0, int(input())):
    string1 = ''
    string = input()
    if len(string) <= 10:
        print(string)
    else:
        string1 += string[0];
        string1 += str((len(string) - 2))
        string1 += string[-1]
        print(string1)