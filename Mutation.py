#Each minion has an intrinsic characteristic value (similar to our DNA), which is an integer.
# The transmogrifier adds an integer K to each of the minions' characteristic value.
#Gru knows that if the new characteristic value of a minion is divisible by 7, then it will have Wolverine-like mutations.
#Given the initial characteristic integers of N minions, all of which are then transmogrified, find out how many of them become Wolverine-like.
number_minions = int(input())
k = int(input("enter the value to be added to the intrinsic value"))
charst_value = [int(x) for x in input().split()]
newValue = [x+k for x in charst_value]
Wolverine_like = 0
for value in newValue:
    if value % 7 == 0:
        Wolverine_like += 1
print(Wolverine_like)
