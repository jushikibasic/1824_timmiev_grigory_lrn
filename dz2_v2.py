def result_func():
    result = 0
    for value in data:
        summ = 0
        for place in str(value):
            summ += int(place)
        if summ % 7 == 0:
            result += value
    return result
data = []
for count in range(1, 1000, 2):
    data.append(count ** 3)
print("Задание а):")
print(result_func())
print("Задание б/c):")
data[:] = [numb + 17 for numb in data]
print(result_func())