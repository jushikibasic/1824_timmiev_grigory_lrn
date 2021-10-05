task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
task_list.reverse()
for value in task_list:
    if ord(value[-1]) in range(48, 58):
        task_list.insert((task_list.index(value) + 1), '"')
task_list.reverse()
for value in task_list:
    if ord(value[-1]) in range(48, 58):
        task_list.insert((task_list.index(value) + 1), '"')
for value in task_list:
    if ord(value[0]) == 43 or ord(value[0]) == 45:
        new = int(value[1:])
        new_value = '{:02d}'.format(new)
        index = task_list.index(value)
        task_list[index] = value[:1] + new_value
for value in task_list:
    if ord(value[0]) in range(48, 58):
        new = int(value)
        new_value = '{:02d}'.format(new)
        index = task_list.index(value)
        task_list[index] = new_value
result = ' '.join(task_list)
print(result)
