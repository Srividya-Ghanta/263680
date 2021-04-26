#a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.
n = int(input())
weapons = [int(x) for x in input().split()]
luck = 0
unlucky = 0
for i in weapons:
    if i % 2 == 0:
        lucky += 1
    else:
        unlucky += 1
if lucky > unlucky:
    print("Ready for the battle")
else:
    print("Not ready for the battle")