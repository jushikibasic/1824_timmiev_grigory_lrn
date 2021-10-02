data = []
step = 0
order = 0
check = None
while step < 1000:
    if step % 2 > 0:
        cube = step ** 3
        data.append(cube)
    step += 1
print("Задание а):")
for value in data:
    check = value ** (1. / 3)
    order += 1
    summ = 0
    count = value
    while count > 0:
        digit = count % 10
        summ += digit
        count = count // 10
    if summ % 7 == 0:
        print('Значение №:'+ str(order) +') равное:'+str(value), 'и являющееся кубом числа:'+ str(round(check)))
        print('Сумма всех его знаков равна:', str(summ) +', она делится на 7 без остатка.')

print("Задание б/c):")
order = 0
for numb in range(len(data)):
    data[numb] = data[numb] +17
for value in data:
    order += 1
    summ = 0
    count = value
    while count > 0:
        digit = count % 10
        summ += digit
        count = count // 10
    if summ % 7 == 0:
        print('Значение №:' + str(order) + ') равное:' + str(value))
        print('Сумма всех его знаков равна:', str(summ) + ', она делится на 7 без остатка.')
