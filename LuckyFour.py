#He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4 in the decimal representation. He is too busy now, so please help him.
def countFour(number):
    return number.count("4")
for i in range(int(input())):
    number = input()
    print(countFour(number))