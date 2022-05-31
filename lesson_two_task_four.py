workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for worker in workers:
    str_name = ''.join(reversed(worker))
    str_name = str_name.partition(' ')[0]
    name = str_name[::-1].lower().capitalize()
    print(f'Привет {name}!')


