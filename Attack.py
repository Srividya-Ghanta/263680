#Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door.
#  Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, 
# and he withdrew in panic.How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

count = 0
for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        count += 1
print(count)