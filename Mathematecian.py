#In his contest he gave the contestants many different pairs of numbers. Each number is made from digits 0 or 1.
#  The contestants should write a new number corresponding to the given pair of numbers.
#  The rule is simple: The i-th digit of the answer is 1 if and only if the i-th digit of the two given numbers differ.
#  In the other case the i-th digit of the answer is 0.
num1 = list(input())
num2 = list(input())
ans = ''
for i in range(0, len(num1)):
    if num1[i] == num2[i]:
        ans += '0'
    else:
        ans += '1'
print(ans)