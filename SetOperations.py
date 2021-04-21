# GIven a string as input if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female.
string = set(input())
if len(string) % 2 == 0:
    print("It is a female")
else:
    print("It is a male")