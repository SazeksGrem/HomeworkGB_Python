worker = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
correct = {}
for i in worker:
    correct = i.split()[-1].capitalize()
    print(f'Привет, {correct}')
