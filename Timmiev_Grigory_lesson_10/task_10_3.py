class Cell:
    def __init__(self, cell_numbs: int):
        self.cells = cell_numbs

    def __str__(self):
        return f'в данной клетке: {self.cells} ячеек'

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} not  a Cell class')
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} not a Cell class')
        if not self.cells - other.cells > 0:
            print('разность клеток 0 или меньше')
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} not a Cell class')
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        """целочмсленное"""
        if not isinstance(other, Cell):
            raise TypeError(f'{other} not a Cell class')
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} not a Cell class')
        return Cell(int(self.cells / other.cells))

    def make_order(self, n):
        lines = self.cells // n
        rest = self.cells % n
        result = ''
        for i in range(lines):
            result += f'{chr(42) * n }\n'
        result += f'{chr(42) * rest}\n'
        return result


cell = Cell(15)
a = Cell(10)
b = Cell(3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(cell.make_order(5))
