def odd_nums(n: int):
    nums_gen = (num for num in range(1, n + 1, 2))
    print("nums_gen это:", type(nums_gen))
    for n in range(1, n + 1, 2):
        print(next(nums_gen))


inp_data = input('Введите число "n": ')
if inp_data.isdigit():
    inp_data = int(inp_data)
    odd_nums(inp_data)
else:
    print("К вводу допускаются только числа")
