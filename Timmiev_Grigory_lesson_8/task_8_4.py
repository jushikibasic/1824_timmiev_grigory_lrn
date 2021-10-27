def val_checker(func):
    def my_deco(*args):
        result = []
        for item in args:
            z = (lambda x: x > 0)(item)
            if z is True:
                result.append(func(item))
            else:
                raise ValueError(f'wrong val {item}')
        return result
    return my_deco


@val_checker
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(*a, sep=', ')
