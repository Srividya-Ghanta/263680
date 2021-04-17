def swap_case(s):
    string = ""
    for i in range(len(s)):
        if (s[i].isalpha()):
            if(s[i].isupper()):
                string = string + chr(ord(s[i])+32)
            else:
                string = string + chr(ord(s[i])-32)
        else:
            string = string + s[i]
    return string
s = input()
result = swap_case(s)
print(result)