#The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.
amount, balance = [x for x in input().split()]
amount = int(amount)
balance = float(balance)
if amount % 5 == 0:
    balance = balance - (amount + 0.50)
    print("{0:.2f}".format(balance))
else:
    print("{0:.2f}".format(balance))