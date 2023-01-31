import math

ax = float(input('Введите координаты точки A по оси x: '))
ay = float(input('Введите координаты точки A по оси y: '))
bx = float(input('Введите координаты точки B по оси x: '))
by = float(input('Введите координаты точки B по оси y: '))

dist = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точками A и B = {round(dist, 3)}')