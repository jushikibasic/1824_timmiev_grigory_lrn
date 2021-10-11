from cbr_parser.utils import extract_data


def currency_rates(code: str) -> str:
    code = code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    val = extract_data("Value")
    zip_res = zip(ch_code, val)
    for name, value in zip_res:
        data.setdefault(name, value)
    return str(data[code])


if __name__ == '__main__':
    currency_rates(__name__)
