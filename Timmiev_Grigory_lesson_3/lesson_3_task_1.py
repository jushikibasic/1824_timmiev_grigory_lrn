def num_translate(num: str) -> None:
    """переводит числительное с английского на русский """
    translate_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
    }
    num = num.lower()
    if num in translate_dict:
        print(num, "переводится как:", (translate_dict[num]))


num_translate(input('Введите английское числительное: '))
