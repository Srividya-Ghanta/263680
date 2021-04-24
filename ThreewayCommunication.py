import math
for i in range(int(input())):
    range = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    ab = math.sqrt((abs(ax-bx)**2+abs(ay-by)**2))
    bc = math.sqrt((abs(bx-cx)**2+abs(by-cy)**2))
    ac = math.sqrt((abs(ax-cx)**2+abs(ay-cy)**2))
    if ab <= range and ac <= range:
        print("yes")
    elif ab <= range and bc <= range:
        print("yes")
    elif ac <= range and bc <= range:
        print("yes")
    else:
        print("no")