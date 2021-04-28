def firstrepeatedChar(str):
    h = {}
    for ch in str:
        if ch in h:
            return ch
        else:
            h[ch] = 1
    return "No repated character"
print(firstRepeatedChar(input("Enter a string : ")))