"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

a = 5
b = 'Hello!'
c = 0.155
d = False
e = None
print(f'Задан список элементов: [{a}, {b}, {c}, {d}, {e}]')
print(f'Элемент {a} имеет {type(a)}')
print(f'Элемент {b} имеет {type(b)}')
print(f'Элемент {c} имеет {type(c)}')
print(f'Элемент {d} имеет {type(d)}')
print(f'Элемент {e} имеет {type(e)}')