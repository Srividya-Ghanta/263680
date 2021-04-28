#"H" prints "Hello, World!",
#"Q" prints the source code of the program itself,
#"9" prints the lyrics of "99 Bottles of Beer" song,
#"+" increments the value stored in the internal accumulator.
#Instructions "H" and "Q" are case-sensitive and must be uppercase. The characters of the program which are not instructions are ignored.
#You are given a program written in HQ9+. You have to figure out whether executing this program will produce any output

string = input()
count = 0
for i in string:
    if i == 'H' or i == 'Q' or i == '9':
        count = 1
        print('YES')
        break
if count == 0:
    print('NO')