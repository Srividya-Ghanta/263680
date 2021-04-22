number = input()
if number == "0":
    print("The number is zero")
elif "." in number:
    print("It is a floating value")
elif "+" in number:
    print("it is a complex value")
elif number.isdecimal():
    print("It is a real number")
else:
    print("entered value is a string")