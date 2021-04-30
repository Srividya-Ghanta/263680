# the store sells horseshoes of all colors under the sun and Valera has enough money to buy any four of them.
# However, in order to save the money, he would like to spend as little money as possible, so you need to help Valera and
# determine what is the minimum number of horseshoes he needs to buy to wear four horseshoes of different colors to a party.
shoe_colour = [int(x) for x in input().split()]
shoe_colour = set(shoe_colour)
if len(shoe_colour) == 4:
    print('0')
else:
    print(abs(4 - len(shoe_colour)))