from cbr_parser.utils import extract_data


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
    new_data = str(data[code]).replace(",", ".")
    return float(new_data)


print(currency_rates(input("введите международный код валюты :")))
