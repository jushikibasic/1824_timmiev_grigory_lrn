def for_(name, fun):
    print(f'{fun.__name__}({name}: {type(fun(name))})')


def type_logger(func):
    def abracadabra(*args, **kwargs):
        result = []
        for item in args:
            for_(item, func)
            result.append(func(item))
        for _, value in kwargs.items():
            for_(value, func)
            result.append(func(value))
        return result
    return abracadabra


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 6, g=3)
print(*a, sep=', ')
