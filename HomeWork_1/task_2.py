seconds = input('Введите время в секундах: ')
# можно сразу в первой строке перевести секунды в int()
days = int(seconds) / (3600*24)
hours = int(seconds) / 3600
minutes = int(seconds) / 60
print(f'Время в формате д:ч:м:с - {days} : {hours} : {minutes} : {seconds}')