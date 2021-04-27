# in the given string, consisting if uppercase and lowercase Latin letters, it:
#deletes all the vowels,
#inserts a character "." before each consonant,
#replaces all uppercase consonants with corresponding lowercase ones.
string = list(input())
string1 = []
vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
for i in range(len(string)):
    if string[i] in vowels:
        string[i] = " "
    if string[i] != " ":
        string1.append(string[i])
string1 = '.'.join(string1)

string1 = string1.lower()
print(string1)
