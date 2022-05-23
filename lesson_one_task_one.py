duration = 0
while duration <= 0:
    duration = int(input('Введите целое количество секунд - '))
    days, hours, minutes, seconds = duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60
    if duration <= 0:
        print('Введенное число должно быть больше нуля.')
    elif duration < 60:
        print(f'{seconds} сек.')
    elif duration < 3600:
        print(f'{minutes} мин., {seconds} сек.')
    elif duration < 86400:
        print(f'{hours} час., {minutes} мин., {seconds} сек.')
    else:
        print(f'{days} дн., {hours} час., {minutes} мин., {seconds} сек.')