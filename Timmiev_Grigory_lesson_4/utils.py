from cbr_parser.utils import extract_data, extract_date


def currency_rates(code: str):
    code = code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    val = extract_data("Value")
    zip_res = zip(ch_code, val)
    for name, value in zip_res:
        data.setdefault(name, value)
    if code in data:
        new_data = float(str(data[code]).replace(",", "."))
        return new_data, extract_date()
    else:
        return None, extract_date()


if __name__ == '__main__':
    cur_cost, cur_date = currency_rates('Name')
    print(cur_cost, cur_date, sep=', ')
