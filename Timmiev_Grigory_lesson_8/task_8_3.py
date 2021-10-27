def type_logger(func):
    def abracadabra(*args, **kwargs):
        result = []
        for item in args:
            try:
                print(f'{func.__name__}({item}: {type(item)})')
                result.append(func(item))
            except TypeError as err:
                print(f'{err}: "{item}"  is {type(item)}')
        for _, value in kwargs.items():
            try:
                print(f'{func.__name__}({value}: {type(value)})')
                result.append(func(value))
            except TypeError as err:
                print(f'{err} {value} type is {type(value)}')
        return result
    return abracadabra


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, '6', 6, g=3)
print(*a, sep=', ')
