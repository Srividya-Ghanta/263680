#Chef belongs to a very rich family which owns many gold mines. 
# Today, he brought N gold coins and decided to form a triangle using these coins. Isn't it strange?
#Chef has a unusual way of forming a triangle using gold coins, which is described as follows:
#He puts 1 coin in the 1st row.
#then puts 2 coins in the 2nd row.
#then puts 3 coins in the 3rd row.

for i in range(int(input())):
    n = int(input())
    for j in range(1, n+1):
        if ((j * (j + 1))//2) == n:
            print(j)
            break
        elif ((j * (j + 1))//2) > n:
            print(j-1)
            break