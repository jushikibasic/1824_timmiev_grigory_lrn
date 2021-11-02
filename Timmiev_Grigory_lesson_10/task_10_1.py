# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
list_1 = [[10, 2, 3], [3, 5, 6]]

print(list_1)


class Matrix:
    def __init__(self, list_in):
        for n in range(len(list_in)):
            list(n)
            self.line = n

    def show(self):
        print(self.line)


a = Matrix(list_1)
a.show()
