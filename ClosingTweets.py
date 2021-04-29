#There are N tweets on the page and each tweet can be opened by clicking on it, to see some statistics related to that tweet.
# Initially all the tweets are closed. Clicking on an open tweet closes it and clicking on a closed tweet opens it. 
# There is also a button to close all the open tweets. Given a sequence of K clicks by Jack, Evan has to guess the total number
#  of open tweets just after each click. Please help Evan in this game.
n, k = map(int, input().split())
arr = []
for i in range(1, k+1):
    string = input()
    if string != 'CLOSEALL':
        temp = string.split()
        if temp[1] in arr:
            arr.remove(temp[1])
        else:
            arr.append(temp[1])
    else:
        arr.clear()
    print(len(arr))