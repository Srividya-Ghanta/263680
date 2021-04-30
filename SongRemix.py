#Let's assume that a song consists of some number of words. 
# To make the dubstep remix of this song, Vasya inserts a certain number of words "WUB" 
# before the first word of the song (the number may be zero), after the last word (the number may be zero),
#  and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, 
# including "WUB", in one string and plays the song at the club.
string = input()
string2 = string.replace('WUB', ' ')
string2 = string2.strip()
print(string2)