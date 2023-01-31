coord_x = int(input('Введите координату точки х: '))
coord_y = int(input('Введите координату точки y: '))
if coord_x == 0 and coord_y == 0:
    print('Точка лежит на пересечении координатных осей X и Y')
elif coord_x == 0:
    print('Точка лежит на координатной оси X')
elif coord_y == 0:
    print('Точка лежит на координатной оси Y')
elif coord_x > 0 and coord_y > 0:
    print(f'Точка ({coord_x},{coord_y}) лежит в первой четверти')
elif coord_x < 0 and coord_y > 0:
    print(f'Точка ({coord_x},{coord_y}) лежит во второй четверти')
elif coord_x < 0 and coord_y < 0:
    print(f'Точка ({coord_x},{coord_y}) лежит в третьей четверти')
elif coord_x > 0 and coord_y < 0:
    print(f'Точка ({coord_x},{coord_y}) лежит в четвертой четверти')