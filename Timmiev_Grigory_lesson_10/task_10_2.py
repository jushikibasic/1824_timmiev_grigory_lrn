class Clothes:
    def __init__(self):
        self.res = None

    def __str__(self):
        return f'расход ткани на {self.__class__.__name__}:\n\t{self.res}'

    def __add__(self, other):
        if not isinstance(other, Clothes):
            raise TypeError(f'{other} not  a Clothes class')
        result = round(self.res + other.res, 3)
        return f'всего ткани потребуется:\n\t{result}'


class Coat(Clothes):
    def __init__(self, value):
        super(Coat, self).__init__()
        self.res = round(value / 6.5 + 0.5, 3)


class Jacket(Clothes):
    def __init__(self, high):
        super(Jacket, self).__init__()
        self.res = round(2 * high + 0.3, 3)


coat = Coat(10)
jacket = Jacket(5)
print(coat)
print(jacket)
print(coat + jacket)
