data = []
step = 0
result1 = 0
result2 = 0
while step < 1000:
    if step % 2 > 0:
        cube = step ** 3
        data.append(cube)
    step += 1
print("Задание а):")
for value in data:
    summ = 0
    count = value
    while count > 0:
        digit = count % 10
        summ += digit
        count = count // 10
    if summ % 7 == 0:
        result1 = result1 + value
print(result1)
print("Задание б/c):")
for numb in range(len(data)):
    data[numb] = data[numb] +17
for value in data:
    summ = 0
    count = value
    while count > 0:
        digit = count % 10
        summ += digit
        count = count // 10
    if summ % 7 == 0:
        result2 = result2 + value
print(result2)