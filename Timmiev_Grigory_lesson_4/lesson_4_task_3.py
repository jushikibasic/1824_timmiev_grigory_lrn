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
        new_data = round(float(str(data[code]).replace(",", ".")), 2)
        return new_data, extract_date()
    else:
        return None, extract_date()


val_code = input("введите международный код валюты :")
cur_cost, cur_date = (currency_rates(val_code))
print(cur_cost, cur_date, sep=', ')
