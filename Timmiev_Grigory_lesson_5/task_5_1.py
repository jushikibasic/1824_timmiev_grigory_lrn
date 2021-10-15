def odd_nums(n: int):
    for _ in range(1, n + 1, 2):
        yield _


inp_data = input('Введите число "n": ')
if inp_data.isdigit():
    inp_data = int(inp_data)
    odd_to_n = odd_nums(inp_data)
    print("odd_to_n, это :", type(odd_to_n))
    for _ in range(0, inp_data + 1, 2):  # inp_data + 2 чтоб генератор выдал StopIteration
        print(next(odd_to_n))
else:
    print("К вводу допускаются только числа")
