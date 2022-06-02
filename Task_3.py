import random

def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []
    for i in range(number):
        word_one = random.choice(nouns)
        jokes.append(word_one)
        word_two = random.choice(adverbs)
        jokes.append(word_two)
        word_three = random.choice(adjectives)
        jokes.append(word_three)
    return jokes

print(get_jokes(1))