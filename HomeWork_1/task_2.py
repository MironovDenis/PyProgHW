seconds = int(input('Введите время в секундах: '))
days = seconds / (3600 * 24)
hours = seconds / 3600
minutes = seconds / 60
print(f'Время в формате д:ч:м:с - {days} : {hours} : {minutes} : {seconds}')
