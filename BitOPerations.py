#initial value of x = 0 and the first line of input is n that specifies the nuber of statements gives
#the given statements can be ++x or x++ or --x ot x-- depending on the statement perform the operations
x = 0
for i in range(0, int(input())):
    string = input()
    if string == '++X' or string == 'X++':
        x += 1
    elif string == '--X' or string == 'X--':
        x -= 1
print(x)