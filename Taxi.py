#Each car can carry at most four passengers. What minimum number of cars will the children need 
# if all members of each group should ride in the same taxi (but one taxi can take more than one group)?

input();a,b,c,d=map(input().count,('1','2','3','4'))
print(d+c+(b*2+max(0,a-c)+3)//4)
