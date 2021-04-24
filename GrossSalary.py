for i in range(int(input())):
    salary = int(input())
    if salary < 1500:
        gross = salary + ((10 * salary) + (90 * salary))/100
    else:
        gross = salary + 500 + (98*salary)/100
    print('%.2f'%gross)