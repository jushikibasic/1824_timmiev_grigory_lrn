src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for name in range(len(src)):
    new_name = src[name]
    if name == len(src) - 1:
        next_name = new_name
    else:
        next_name = src[name + 1]
    if new_name < next_name:
        result.append(next_name)
print(result)
