task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name in task_list:
    new_name = ''
    work_name = name[::-1]
    for letter in work_name:
        new_name += letter
        if ord(letter) == 32:
            new_name = new_name[::-1]
            break
    print('Привет,' + new_name.title() + '!')
