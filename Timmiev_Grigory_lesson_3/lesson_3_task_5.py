import random


def get_jokes(count_jokes: int, no_copies=1) -> None:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    thing_jk = []
    time_jk = []
    about_thing_jk = []
    for step in range(count_jokes):
        thing_jk.append(random.sample(nouns, no_copies))
        time_jk.append(random.sample(adverbs, no_copies))
        about_thing_jk.append(random.sample(adjectives, no_copies))
        print(thing_jk)
        print(time_jk)
        print(about_thing_jk)



get_jokes(2)
#get_jokes(5)
