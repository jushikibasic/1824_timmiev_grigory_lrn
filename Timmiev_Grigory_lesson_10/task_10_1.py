# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
list_1 = [[10, 2, 3], [3, 5, 6]]
# pos = [i for i in range(len(list_in))]
# for item in pos:


class Matrix:
    def __init__(self, list_in):
        self.line = list_in

    def __str__(self):
        # res = [i for i in self.line]
        for item in self.line:
            i = "\n".join(str(item))
        return i


a = Matrix(list_1)
#for bottle in our_bottles:
print(f'\t{a}')
# a.show()
