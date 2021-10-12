from utils import currency_rates


def upg_cur_rates(argv: str):
    program, arg = argv
    ph_cost, ph_date = currency_rates(arg)
    return ph_cost, ph_date


if __name__ == '__main__':
    import sys
    cur_cost, cur_date = upg_cur_rates(sys.argv)
    exit(print(cur_cost, cur_date, sep=', '))
