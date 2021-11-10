from my_exceptions import ZeroDivExcept


def div(a, b):
    try:
        if b == 0:
            raise ZeroDivExcept
        return a / b
    except ZeroDivExcept as er:
        print(er)


print(div(4, 0))
print(div(4, 2))
