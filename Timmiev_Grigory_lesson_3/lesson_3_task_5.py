import random


def get_jokes(count_jokes: int, **kwargs) -> None:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    counts = kwargs.get('counts', 1)
    if counts > 5:
        counts = 1
    for step in range(count_jokes):
        thing = random.sample(nouns, counts)
        time = random.sample(adverbs, counts)
        about = random.sample(adjectives, counts)
        seq = "{} {} {}".format(thing, time, about)
        data.append(seq)
    print(data)


get_jokes(5, counts=4)
get_jokes(5)
