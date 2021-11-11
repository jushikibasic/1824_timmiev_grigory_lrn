from my_exceptions import MyValEr


def numbers_in():
    numbers_list = []
    while True:
        x = input('введите число :').capitalize()
        if x == 'Stop':
            break
        try:
            if not x.isdigit():
                raise MyValEr
            numbers_list.append(int(x))
        except MyValEr as er:
            print(er)
    return numbers_list


data = numbers_in()
print(data)
