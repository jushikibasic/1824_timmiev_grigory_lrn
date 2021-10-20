from utils import extract_data


def currency_rates(code: str):
    code = code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    val = extract_data("Value")
    zip_res = zip(ch_code, val)
    for name, value in zip_res:
        data.setdefault(name, value)
    if code in data:
        new_data = str(data[code]).replace(",", ".")
        return round(float(new_data), 2)
    else:
        return None


print(currency_rates(input("введите международный код валюты :")))
