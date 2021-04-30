#Little X can pass only p levels of the game. And Little Y can pass only q levels of the game.
#  You are given the indices of levels Little X can pass and the indices of levels Little Y can pass.
#  Will Little X and Little Y pass the whole game, if they cooperate each other?
n = int(input())
plevels = [int(x) for x in input().split()]
qlevels = [int(x) for x in input().split()]
del plevels[0]
del qlevels[0]
combined = plevels + qlevels
combined = list(set(combined))
if len(combined) == n:
    print("they pass all the levels with cooperation.")
else:
    print("They do not pass all the levels.")