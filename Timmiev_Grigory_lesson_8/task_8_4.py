from functools import wraps


def val_checker(func):
    @wraps(func)
    def my_deco(*args):
        result = []
        for item in args:
            try:
                if item > 0:
                    result.append(func(item))
                else:
                    raise ValueError(f'wrong val {item}')
            except TypeError as err:
                print(f'{err} {item} type is {type(item)}')
            return result
    return my_deco


@val_checker
def calc_cube(x):
    return x ** 3


a = calc_cube('ss')
print(*a, sep=', ')
