#if n = 1, then his feeling is "I hate it" or if n = 2 it's "I hate that I love it", and if n = 3 it's 
# "I hate that I love that I hate it" and so on.
n = int(input())
ans = ''
for i in range(1, n+1):
    if i % 2 != 0:
        ans += 'I hate '
    else:
        ans += 'I love '
    if i != n:
        ans += 'that '
ans += 'it'
print(ans)