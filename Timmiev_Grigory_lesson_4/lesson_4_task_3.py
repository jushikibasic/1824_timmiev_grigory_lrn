from cbr_parser.utils import extract_data, extract_date


def currency_rates(code: str):
    code = code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    val = extract_data("Value")
    zip_res = zip(ch_code, val)
    if code not in ch_code:
        return None
    for name, value in zip_res:
        data.setdefault(name, value)
    new_data = float(str(data[code]).replace(",", "."))
    return extract_date(), new_data


val_code = input("введите международный код валюты :")
cur_date, cur_cost = (currency_rates(val_code))
print(cur_date, cur_cost)
