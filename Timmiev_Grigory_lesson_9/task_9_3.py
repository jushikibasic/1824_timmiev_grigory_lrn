income_welder = {'wage': 50000, 'bonus': 15000}
income_driver = {'wage': 30000, 'bonus': 7500}
income_scientist = {'wage': 150000, 'bonus': 25000}


class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


welder = Position('Иван', 'Васильев', 'сварщик', income_welder)
driver = Position('Петр', 'Николаев', 'водитель', income_driver)
scientist = Position('Геннадий', 'Разумов', 'ученый', income_scientist)
print(welder.get_full_name(), welder.get_total_income())
print(driver.get_full_name(), driver.get_total_income())
print(scientist.get_full_name(), scientist.get_total_income())
