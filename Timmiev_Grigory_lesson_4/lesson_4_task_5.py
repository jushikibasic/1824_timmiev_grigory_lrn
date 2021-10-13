from cbr_parser.utils import extract_date
from utils import currency_rates


def upg_cur_rates(argv: str):
    program, arg = argv
    ph_cost, ph_date = currency_rates(arg)
    return ph_cost, ph_date


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        cur_cost, cur_date = upg_cur_rates(sys.argv)
    else:
        cur_cost = None
        cur_date = extract_date()
    exit(print(cur_cost, cur_date, sep=', '))
