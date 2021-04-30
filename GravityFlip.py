#There are n columns of toy cubes in the box arranged in a line. The i-th column contains ai cubes.
#  At first, the gravity in the box is pulling the cubes downwards. 
# When Chris switches the gravity, it begins to pull all the cubes to the right side of the box.
#  The figure shows the initial and final configurations of the cubes in the box: the cubes that have changed their position 
# are highlighted with orange.
#Given the initial configuration of the toy cubes in the box, find the amounts of cubes in each of the n columns after the gravity switch!
num = int(input())
arr= [int(x) for x in input().split()]
s = ' '.join(str(i) for i in sorted(arr))
print(s)