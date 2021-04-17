import builtins
n = int(input())
integer_list = map(int, input().split())
integer_list = tuple(integer_list)
print(builtins.hash(integer_list))