#Первый вариант
duration = int(input('Введите количество секуд' ))
sec = duration
minute = duration // 60
hour = duration // 3600
day = duration // 86400

if sec < 60:
    print(f'{sec} сек')
elif 60 <= sec <= 3599:
    print(f'{minute} мин {sec % 60} сек')
elif 3600 <= sec <= 86399:
    print(f'{hour % 24} час {minute % 60} мин {sec % 60} сек')
else:
    print(f'{day} дн {hour % 24} час {minute % 60} мин {sec % 60} сек')


#Второй вариант

duration = int(input('Введите количество секуд' ))
sec = duration % 60
minute = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 86400
print(f'{day} дн {hour} час {minute} мин {sec} сек')

