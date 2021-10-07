def adv_translate(numb: str) -> None:
    """переводит числительное с английского на русский """
    translate_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
    }
    if numb[0].isupper():
        numb = numb.lower()
        if numb in translate_dict:
            print(numb.capitalize(), "переводится как:", (translate_dict[numb]).capitalize())
    else:
        numb = numb.lower()
        if numb in translate_dict:
            print(numb, "переводится как:", (translate_dict[numb]))


adv_translate(input('Введите английское числительное: '))
