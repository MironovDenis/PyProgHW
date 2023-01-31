quarter_num = int(input('Введите номер четверти: '))
if 1 > quarter_num or quarter_num > 4:
    print('Введено некорректное значение!')
elif quarter_num == 1:
    print('Первая четверть. Значения Х > 0, Y > 0.')
elif quarter_num == 2:
    print('Вторая четверть. Значения Х < 0, Y > 0.')
elif quarter_num == 3:
    print('Третья четверть. Значения Х < 0, Y < 0.')
else:
    print('Четвертая четверть. Значения Х > 0, Y < 0.')