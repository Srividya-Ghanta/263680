#python program to print who won the match
number = int(input("Enter the number of games played"))
games = input().split('')
if games.count("A") > games.count("D"):
    print("Anton")
elif games.count("D") > games.count("A"):
    print("Dhanik")
else:
    print("It is a draw")