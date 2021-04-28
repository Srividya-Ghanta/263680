#tart with the first n. He writes down the following sequence of numbers: firstly all odd integers from 1 to n (in ascending order), 
# then all even integers from 1 to n (also in ascending order). Help our hero to find out which number 
# will stand at the position number k.
n,k=map(int,input().split());t=(n+1)//2;print(2*k-[1,2*t][k>t])