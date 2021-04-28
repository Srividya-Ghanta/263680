#n this case we should automatically change the case of all letters. For example, the case of the letters that form words "hELLO", "HTTP", "z" should be changed.
#Write a program that applies the rule mentioned above. If the rule cannot be applied, the program should leave the word unchanged.
string = input()
string1 = ''
if string.isupper():
    print(string.lower())
elif len(string) == 1 and string.islower():
    print(string.upper())
elif (string[:1].islower() and string[1:].isupper()):
    string1 += string[:1].upper()
    string1 += string[1:].lower()
    print(string1)
else:
    print(string)