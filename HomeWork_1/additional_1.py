day = int(input('Введите номер дня недели: '))
if day < 1 or day > 7:
    print('Введено некорректное значение!')
elif 1 <= day < 6:
    print('Это будний день.')
elif day == 6 or day == 7:
    print('Это выходной день!!!')