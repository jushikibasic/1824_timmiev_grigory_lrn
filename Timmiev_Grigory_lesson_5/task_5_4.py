from time import perf_counter
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Решение №1
start = perf_counter()
result_2 = [src[num + 1] for num in range(len(src) - 1) if src[num] < src[num + 1]]
print(result_2, perf_counter() - start)

# Решение №2
start = perf_counter()
result = []
for name in range(len(src)):
    new_name = src[name]
    if name == len(src) - 1:
        next_name = new_name
    else:
        next_name = src[name + 1]
    if new_name < next_name:
        result.append(next_name)
print(result, perf_counter() - start)
