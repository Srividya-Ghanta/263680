def firstchar_Change(string):  
    char = string[0]  
    string = string.replace(char, '$')  
    string = char + string[1:]  
    return string  
print(change_char(input()))