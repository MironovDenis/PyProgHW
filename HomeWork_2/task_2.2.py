"""
Задание 2.

Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

number = int(input('Введите целое положительное число: '))
max_num = 0
while number > 0:
    count_num = number % 10
    if count_num > max_num:
        max_num = count_num
    number //= 10
print(f'Самая большая цифра в числе: {max_num}')

