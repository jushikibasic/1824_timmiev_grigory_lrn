def num_translate(num: str) -> str:
    """переводит числительное с английского на русский """
    translate_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
    }
    num = num.lower()
    if num in translate_dict:
        return translate_dict[num]
    else:
        return None


num_in = input('Введите английское числительное: ')
print(num_in, "переводится как:", (num_translate(num_in)))
