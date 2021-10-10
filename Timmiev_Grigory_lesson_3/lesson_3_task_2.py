def num_translate_adv(num: str) -> None:
    """переводит числительное с английского на русский """
    translate_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
    }
    if num[0].isupper():
        num = num.lower()
        if num in translate_dict:
            print(num.capitalize(), "переводится как:", (translate_dict[num]).capitalize())
    else:
        num = num.lower()
        if num in translate_dict:
            print(num, "переводится как:", (translate_dict[num]))


num_translate_adv(input('Введите английское числительное: '))
