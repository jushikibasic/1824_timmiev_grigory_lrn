task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
def mark_placer(list_name):
    list_name.reverse()
    for value in list_name:
        if ord(value[-1]) in range(48, 58):
            list_name.insert((list_name.index(value) + 1), '"')
mark_placer(task_list)
mark_placer(task_list)
for value in task_list:
    if ord(value[0]) in range(48, 58):
        new = int(value)
        new_value = '{:02d}'.format(new)
        index = task_list.index(value)
        task_list[index] = new_value
    if ord(value[0]) == 43 or ord(value[0]) == 45:
        new = int(value[1:])
        new_value = '{:02d}'.format(new)
        index = task_list.index(value)
        task_list[index] = value[:1] + new_value
for name in range(len(task_list)):
    new_name = task_list[name]
    if name == len(task_list) - 1:
        next_name = new_name
    else:
        next_name = task_list[name + 1]
    if new_name == '"' and next_name[-1].isdigit():
        print(task_list[name], end='')
    elif new_name[-1].isdigit():
        print(task_list[name], end='')
    else:
        print(task_list[name], end=' ')
