#There are n drinks in his fridge, the volume fraction of orange juice in the i-th drink equals pi percent.
#Find the volume fraction of orange juice in the final drink.
n = int(input())
drinks = [int(x) for x in input().split()]
orange_percent = 0.0
for i in drinks:
    orange_percent += (i / 100)
total_percent = ((orange_percent / n) * 100)
print("{0:.12f}".format(total_percent))