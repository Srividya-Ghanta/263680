def split_and_join(line):
    line = line.split(" ")
    newline = '-'.join(line)
    return newline
line = input()
result = split_and_join(line)
print(result)