#There are n balloons of two bolours amber and brass
#given a string containing n characters where 'a' represents amber and 'b' represents brass
#  print the minimum number of balloons to be painted so that all the n balloons are of the same colour
number_of_balloons = int(input())
color_pattern = list(input())
amber = color_pattern.count('a')
brass = color_pattern.count('b')
if amber > brass:
    print(brass)
else:
    print(amber)