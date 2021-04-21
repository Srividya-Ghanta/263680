#bobs with is <= liams and bobs's weight triples every year and liams weight doubles every after how many years does bob's weight > liam's
bob, liam = [int(x) for x in input().split()]
year = 0
while(bob <= liam):
    year += 1
    bob = (3 * bob)
    liam = (2 * liam)
print(year)