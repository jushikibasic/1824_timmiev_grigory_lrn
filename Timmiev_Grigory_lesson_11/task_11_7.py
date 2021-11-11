from my_exceptions import NotAComplex


class ComplexNumb:
    def __init__(self, math_a: int, math_b):
        self.math_a = math_a
        self.math_b = math_b

    @staticmethod
    def check(other):
        return isinstance(other, ComplexNumb)

    def __str__(self):
        return f'{self.math_a} + {self.math_b}*i'

    def __add__(self, other):
        try:
            if not ComplexNumb.check(other):
                raise NotAComplex
            else:
                x = self.math_a + other.math_a
                y = self.math_b + other.math_b
                return ComplexNumb(x, y)
        except NotAComplex as er:
            print(f'{other} {er}')

    def __mul__(self, other):
        try:
            if not ComplexNumb.check(other):
                raise NotAComplex
            else:
                x = self.math_a * other.math_a - self.math_b * other.math_b
                y = self.math_a * other.math_b + self.math_b * other.math_a
                return ComplexNumb(x, y)
        except NotAComplex as er:
            print(f'{other} {er}')


a = ComplexNumb(1, 4)
b = ComplexNumb(6, 8)
z = a + b
j = a * b
print(z)
print(j)
