income = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
profit = income - costs
rent = profit / income
if profit < 0:
    print('Фирма работает в убыток :(')
elif profit == 0:
    print('Фирма не получила прибыль')
else:
    print(f'Фирма получила прибыль: {profit}')
    print(f'Рентабельность выручки: {rent}')
    workers = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit / workers}')
