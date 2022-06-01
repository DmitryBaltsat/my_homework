from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num=1):
    """This simple function creates jokes from random words in specified lists, if second argument is true - allows repeats"""
    jokes = []
    for joke in range(num):
        word_one, word_two, word_three = choice(nouns), choice(adverbs), choice(adjectives)
        jokes.append(f'{word_one} {word_two} {word_three}')
    return jokes

print(get_jokes(5))






