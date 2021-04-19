import math
 
leng, bre, side = map(int, input().split())
print(math.ceil(leng / side) * math.ceil(bre / side))