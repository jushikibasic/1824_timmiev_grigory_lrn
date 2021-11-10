from set import RE_DATE
from my_exceptions import WrongDate, DayExcept, MonthExcept, YearExcept


class Data:
    def __init__(self, input_date: str):
        self.date = input_date

    @staticmethod
    def data_valid(input_date):
        try:
            if RE_DATE.match(input_date):
                keys = ['d', 'm', 'y']
                res = dict(zip(keys, input_date.split('-')))
                if int(res['d']) not in range(1, 32):
                    raise DayExcept
                if int(res['m']) not in range(1, 13):
                    raise MonthExcept
                if int(res['y']) not in range(1900, 2500):
                    raise YearExcept
            else:
                raise WrongDate
        except (DayExcept, MonthExcept, YearExcept, WrongDate) as er:
            print(er)
        else:
            return res

    @classmethod
    def extract(cls, input_date, elements=('d', 'm', 'y')):
        try:
            if not Data.data_valid(input_date):
                raise WrongDate
        except WrongDate as er:
            print(er)
        else:
            res = Data.data_valid(input_date)
            return {x: res[x] for x in elements}


print(Data.extract('31-10-2021', ['d', 'm']))
