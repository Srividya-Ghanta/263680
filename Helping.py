#Write a program, which takes an integer N and if the number is less than 10 then display "Thanks for helping Chef!" otherwise print "-1".
test = int(input())
for i in range(test):
    N = int(input())
    if N < 10:
        print("Thanks for helping Chef")
    else:
        print("-1")