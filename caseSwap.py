string = list(input())
up = 0
lo = 0
for i in string:
    if i.isupper():
        up += 1
    else:
        lo += 1
if up > lo:
    string = ''.join(string)
    string.upper()
else:
    string = ''.join(string)
    string.lower()
print(string)