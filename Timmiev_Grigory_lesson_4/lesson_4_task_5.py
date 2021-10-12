from utils import currency_rates


def upg_cur_rates(argv: str) -> float:
    program, arg = argv
    print(currency_rates(arg))


if __name__ == '__main__':
    import sys
    exit(upg_cur_rates(sys.argv))
