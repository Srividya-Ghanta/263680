string = list(input())
up = 0
lo = 0
for i in string:
    if i.isupper():
        up += 1
        #print("IN upper")
    else:
        lo += 1
       # print("In lower")
if up > lo:
    string = ''.join(string)
    string = string.upper()
else:
    string = ''.join(string)
    string = string.lower()
print(string)