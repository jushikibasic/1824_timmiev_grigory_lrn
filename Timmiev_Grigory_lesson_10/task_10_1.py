from itertools import zip_longest
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
list_1 = [[10, 2, 3], [3, 5, 6]]
list_2 = [[20, 4, 6], [6, 10, 12]]


class Matrix:
    def __init__(self, list_in):
        self.line = list_in

    def __str__(self):
        i = ''
        for item in self.line:
            i += ''.join(f'{item}\n')
        return i

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'{other} not  a Matrix class')
        if len(self.line) == len(other.line):
            result = []
            for i in range(len(self.line)):
                if len(self.line[i]) == len(other.line[i]):
                    result.append([x + y for x, y in zip_longest(self.line[i], other.line[i])])
            new = Matrix(result)
            return new


a = Matrix(list_1)
b = Matrix(list_2)
print(a)
print(b)

res = a + b
print(res)
