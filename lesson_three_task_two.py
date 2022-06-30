num_dict = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}


def num_translate():
    num = input('Please enter number - ')
    if num[0].isupper():
        num = num_dict.get(num.lower())
        result = num.capitalize()
        print(f'Перевод - {result}.')
    else:
        result = num_dict.get(num)
        print(f'Перевод - {result}.')


num_translate()