import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
thing_jk = []
time_jk = []
about_thing_jk = []
for step in range(2):
    thing_jk.append(*random.sample(nouns, 1))
    time_jk.append(*random.sample(adverbs, 1))
    about_thing_jk.append(*random.sample(adjectives, 1))
    print('thing', thing_jk)
    print('time', time_jk)
    print('about', about_thing_jk)