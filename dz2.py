def result_func(table):
    result = 0
    for value in table:
        summ = 0
        count = value
        while count > 0:
            summ += count % 10
            count = count // 10
        if summ % 7 == 0:
            result += value
    return result
data = []
step = 0
while step < 1000:
    if step % 2 > 0:
        data.append(step ** 3)
    step += 1
print("Задание а):")
print(result_func(data))
print("Задание б/c):")
for numb in range(len(data)):
    data[numb] += 17
print(result_func(data))