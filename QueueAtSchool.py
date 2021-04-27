# if at time x a boy stands on the i-th position and a girl stands on the (i + 1)-th position, then at time x + 1 the
#  i-th position will have a girl and the (i + 1)-th position will have a boy. The time is given in seconds.
#You've got the initial position of the children, at the initial moment of time. Determine the way the queue is 
# going to look after t seconds.
t=int(input()[2:]);s=input()
while t:s=s.replace('BG','GB');t-=1
print(s)