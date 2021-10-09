import random


def get_jokes(count_jokes: int, no_copies=False) -> None:
    """
    Генерирует шутки комбинируя значения из списков: nouns, adverbs, adjectives
    :param count_jokes: Количество шуток
    :param no_copies: True - запрещает использовать повторы/False -разрешает(по умолчанию)
    """
    thing_jk = []
    time_jk = []
    about_thing_jk = []
    count = len(nouns)
    copies = 1
    new_result = []
    if count_jokes > len(nouns):
        count = count_jokes
    if no_copies is True:
        count = 1
        copies = len(nouns)
    if count_jokes > len(nouns) and no_copies is True:
        print('Установлено условие без повторов. '
              'Для большего количества шуток добавьте'
              'значений в списки')
        count = 1
        copies = len(nouns)
    for step in range(count):
        thing_jk.extend(random.sample(nouns, copies))
        time_jk.extend(random.sample(adverbs, copies))
        about_thing_jk.extend(random.sample(adjectives, copies))
    for thing, time, about in zip(thing_jk, time_jk, about_thing_jk):
        result = list([f'{thing} {time} {about}'])
        new_result.append(*result)
    print(new_result[0:count_jokes])


nouns = ["автомобиль", "лес", "огонь", "город", "дом", "козел"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "давным давно"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "меланхоличный"]
get_jokes(6, True)
