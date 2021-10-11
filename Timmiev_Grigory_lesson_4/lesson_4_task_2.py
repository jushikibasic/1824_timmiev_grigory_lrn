from cbr_parser.utils import extract_data


def currency_rates(code: str) -> float:
    code = code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    val = extract_data("Value")
    zip_res = zip(ch_code, val)
    for name, value in zip_res:
        data.setdefault(name, value)
    new_data = str(data[code]).replace(",", ".")
    return float(new_data)


if __name__ == '__main__':
    import sys
    exit(currency_rates(sys.code))
