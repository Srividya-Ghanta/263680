#A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).
#He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas

k, n, w = [int(x) for x in input().split()]
cost = (w*(w + 1) / 2) * k
if cost >= n:
    print(cost-n,"amount borrowed")
else:
    print("No amount borrowed")
    