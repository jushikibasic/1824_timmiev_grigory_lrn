class MyEx(Exception):
    _default_detail: str = 'ошибка'

    def __init__(self, detail: str = None):
        if detail:
            self._default_detail = detail

    def __str__(self):
        return self._default_detail


class DateError(MyEx):
    _default_detail: str = 'ошибка даты'


class WrongDate(DateError):
    _default_detail: str = 'не корректная дата'


class DayExcept(WrongDate):
    _default_detail: str = 'ошибка дня'


class MonthExcept(WrongDate):
    _default_detail: str = 'ошибка месяца'


class YearExcept(WrongDate):
    _default_detail: str = 'ошибка года'


class ZeroDivExcept(MyEx):
    _default_detail: str = 'Попытка деления на ноль'


class MyValEr(MyEx):
    _default_detail: str = 'Допускаются только числа'
